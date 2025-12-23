from app.services.rule_engine import detect_intent
from app.services.crop_detector import detect_crop
from app.services.mandi_service import get_price_by_crop
from app.services.trend_service import analyze_trend
from app.services.confidence_service import calculate_confidence
from app.config import GEMINI_API_KEY, AI_ENABLED
from app.services.token_service import (
    can_use_ai,
    consume_token,
    tokens_left
)

def handle_chat(
    message: str,
    memory: dict,
    language: str,
    location: dict | None,
    ai_enabled: bool,
    client_ip: str
):
    if memory is None:
        memory = {}

    if location is None:
        location = {}

    intent = detect_intent(message)
    crop = detect_crop(message) or memory.get("lastCrop")

    if not crop:
        return {
            "text": (
                "कृपया फसल का नाम बताएं।"
                if language == "hi"
                else "Please mention the crop name."
            ),
            "memory": memory
        }

    # ---------- PRICE ----------
    if intent == "price":
        data = get_price_by_crop(crop, location)

        if not data:
            return {
                "text": (
                    "डेटा उपलब्ध नहीं है।"
                    if language == "hi"
                    else "No data available."
                ),
                "memory": memory
            }

        # ✅ update memory safely
        memory.update({
            "lastCrop": crop,
            "lastIntent": "price",
            "lastDistrict": data["district"],
            "lastState": data["state"],
            "lastMandi": data["mandi"]
        })

        explanation = None

        # 🔐 AI GATE (ALL must pass)
        if (
            ai_enabled
            and AI_ENABLED
            and GEMINI_API_KEY
            and can_use_ai(client_ip)
        ):
            # 🔥 consume token FIRST
            consume_token(client_ip)

            try:
                from app.services.ai_explainer import explain_price
                from app.services.ai_logger import log_ai_explanation

                explanation = explain_price(data, language)

                if explanation:
                    log_ai_explanation(
                        crop=crop,
                        mandi=data["mandi"],
                        language=language,
                        explanation=explanation
                    )
            except Exception:
                explanation = None


        base_text = (
            f"📍 {data['mandi']} मंडी में {crop} का भाव ₹{data['modalPrice']} प्रति क्विंटल है।"
            if language == "hi"
            else f"📍 {data['mandi']} mandi {crop} price is ₹{data['modalPrice']} per quintal."
        )

        return {
            "text": f"{base_text}\n\n🧠 {explanation}" if explanation else base_text,
            "priceData": data,
            "confidence": calculate_confidence(data["date"]),
            "memory": memory,
            "tokensLeft": tokens_left(client_ip)
        }

    # ---------- TREND ----------
    if intent == "trend":
        data = get_price_by_crop(crop, location)

        if not data:
            return {
                "text": (
                    "ट्रेंड डेटा नहीं है।"
                    if language == "hi"
                    else "Trend data not available."
                ),
                "memory": memory
            }

        trend = analyze_trend(data["minPrice"], data["maxPrice"])

        return {
            "text": (
                f"{crop} की कीमतों का रुझान {trend} है।"
                if language == "hi"
                else f"{crop} price trend is {trend}."
            ),
            "memory": memory
        }

    return {
        "text": (
            "आप भाव या ट्रेंड पूछ सकते हैं।"
            if language == "hi"
            else "You can ask about prices or trends."
        ),
        "memory": memory
    }
