def analyze_trend(min_price: int, max_price: int) -> str:
    diff = max_price - min_price

    if diff >= 300:
        return "up"
    if diff <= 100:
        return "stable"
    return "down"
