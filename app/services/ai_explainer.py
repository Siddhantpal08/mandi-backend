import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def explain_price(data: dict, language: str):
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
