def detect_intent(text: str) -> str:
    t = text.lower()

    if any(x in t for x in ["price", "भाव"]):
        return "price"
    if any(x in t for x in ["sell", "बेच"]):
        return "sell"
    if any(x in t for x in ["trend", "रुझान"]):
        return "trend"
    if any(x in t for x in ["nearby", "paas", "aas paas"]):
        return "nearby"
    if any(x in t for x in ["compare", "better", "behtar"]):
        return "compare"

    return "unknown"
