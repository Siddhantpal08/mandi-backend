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
    f"""
        आप एक कृषि विशेषज्ञ हैं।
        सरल भाषा में किसान को समझाइए:

        फसल: {data['crop']}
        मंडी: {data['mandi']}
        भाव: ₹{data['modalPrice']} प्रति क्विंटल

        कारण बताएं:
        - मांग और आपूर्ति
        - मौसम
        - आवक
        - किसान क्या करें

        भाषा दोस्ताना हो।
        """
            if language == "hi"
            else
            f"""
        You are an agriculture expert.

        Explain to a farmer in simple terms:

        Crop: {data['crop']}
        Mandi: {data['mandi']}
        Price: ₹{data['modalPrice']} per quintal

        Explain:
        - supply & demand
        - arrivals
        - season
        - what farmer should do

        Be friendly, not robotic.
        """
        )


    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
