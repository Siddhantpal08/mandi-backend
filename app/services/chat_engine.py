from app.services.rule_engine import detect_intent
from app.services.crop_detector import detect_crop
from app.services.mandi_service import get_price_by_crop
from app.services.trend_service import analyze_trend
from app.services.confidence_service import calculate_confidence


def handle_chat(
    message: str,
    memory: dict,
    language: str,
    location: dict | None,
    ai_enabled: bool
):
    # ---------------- Detect intent & crop ----------------
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

    # ---------------- PRICE ----------------
    if intent == "price":
        data = get_price_by_crop(crop, location)

        if not data:
            return {
                "text": (
                    "इस फसल के लिए डेटा उपलब्ध नहीं है।"
                    if language == "hi"
                    else "No data available for this crop."
                ),
                "memory": memory
            }

        memory.update({
            "lastCrop": crop,
            "lastMandi": data["mandi"],
            "lastDistrict": data["district"],
            "lastState": data["state"],
            "lastIntent": "price"
        })

        explanation = None
        if ai_enabled:
            from app.services.ai_explainer import explain_price
            explanation = explain_price(data, language)

        base_text = (
            f"📍 {data['mandi']} मंडी में {crop} का भाव ₹{data['modalPrice']} प्रति क्विंटल है।"
            if language == "hi"
            else f"📍 {data['mandi']} mandi {crop} price is ₹{data['modalPrice']} per quintal."
        )

        final_text = (
            f"{base_text}\n\n🧠 {explanation}"
            if explanation
            else base_text
        )

        return {
            "text": final_text,
            "priceData": data,
            "confidence": calculate_confidence(data["date"]),
            "memory": memory
        }

    # ---------------- TREND ----------------
    if intent == "trend":
        data = get_price_by_crop(crop, location)

        if not data:
            return {
                "text": (
                    "ट्रेंड डेटा उपलब्ध नहीं है।"
                    if language == "hi"
                    else "Trend data not available."
                ),
                "memory": memory
            }

        trend = analyze_trend(
            data["minPrice"],
            data["maxPrice"]
        )

        return {
            "text": (
                f"{crop} की कीमतों का रुझान {trend} है।"
                if language == "hi"
                else f"{crop} price trend is {trend}."
            ),
            "memory": memory
        }

    # ---------------- SELL ----------------
    if intent == "sell":
        return {
            "text": (
                f"{crop} के लिए अगले 7–10 दिन में बेचने पर बेहतर मौका मिल सकता है।"
                if language == "hi"
                else f"Selling {crop} in the next 7–10 days may be beneficial."
            ),
            "memory": memory
        }

    # ---------------- NEARBY ----------------
    if intent == "nearby":
        # Nearby logic can be improved later with geo-distance
        return {
            "text": (
                "पास की मंडियों का फीचर जल्द आ रहा है।"
                if language == "hi"
                else "Nearby mandi feature is coming soon."
            ),
            "memory": memory
        }

    # ---------------- FALLBACK ----------------
    return {
        "text": (
            "आप भाव, ट्रेंड या बेचने से जुड़ा सवाल पूछ सकते हैं।"
            if language == "hi"
            else "You can ask about prices, trends, or selling advice."
        ),
        "memory": memory
    }
