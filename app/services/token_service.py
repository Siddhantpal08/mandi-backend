from datetime import date
from collections import defaultdict

DAILY_LIMIT = 10

# { "ip|date": count }
_usage = defaultdict(int)

def get_token_key(ip: str):
    return f"{ip}|{date.today().isoformat()}"

def can_use_ai(ip: str) -> bool:
    key = get_token_key(ip)
    return _usage[key] < DAILY_LIMIT

def consume_token(ip: str):
    key = get_token_key(ip)
    _usage[key] += 1

def tokens_left(ip: str) -> int:
    key = get_token_key(ip)
    return max(0, DAILY_LIMIT - _usage[key])
