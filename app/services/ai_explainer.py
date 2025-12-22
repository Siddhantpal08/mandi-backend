def explain_price(data: dict, language: str):
    try:
        import google.generativeai as genai
    except ImportError:
        return None  # AI not available in production

    from app.config import GEMINI_API_KEY

    if not GEMINI_API_KEY:
        return None

    genai.configure(api_key=GEMINI_API_KEY)

    prompt = (
        f"Explain in simple Hindi why {data['crop']} price is "
        f"{data['modalPrice']} in {data['mandi']} mandi."
        if language == "hi"
        else
        f"Explain simply why {data['crop']} price is "
        f"{data['modalPrice']} in {data['mandi']} mandi."
    )

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
