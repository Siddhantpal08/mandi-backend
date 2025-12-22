import google.generativeai as genai
from app.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def explain_price(data: dict, language: str) -> str | None:
    if not GEMINI_API_KEY:
        return None

    prompt = (
        f"Explain today's mandi price to a farmer in simple "
        f"{'Hindi' if language == 'hi' else 'English'}.\n\n"
        f"Crop: {data['crop']}\n"
        f"Mandi: {data['mandi']}\n"
        f"Modal Price: {data['modalPrice']} INR/quintal\n\n"
        f"Keep it short, factual, and non-advisory."
    )

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return None
