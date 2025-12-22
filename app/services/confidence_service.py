from datetime import datetime

def calculate_confidence(date_str: str) -> str:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    days_old = (datetime.now() - date).days

    if days_old <= 2:
        return "High"
    if days_old <= 7:
        return "Medium"
    return "Low"
