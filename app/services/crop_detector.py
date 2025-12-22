def detect_crop(text: str) -> str | None:
    t = text.lower()

    if "wheat" in t or "गेहूं" in t:
        return "wheat"
    if "soybean" in t or "सोयाबीन" in t:
        return "soybean"
    if "paddy" in t or "धान" in t:
        return "paddy"

    return None
