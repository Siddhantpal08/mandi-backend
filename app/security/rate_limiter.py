import time
from collections import defaultdict

# max AI calls per IP per window
AI_LIMIT = 5
WINDOW_SECONDS = 60

_requests = defaultdict(list)

def allow_ai_request(ip: str) -> bool:
    now = time.time()
    window_start = now - WINDOW_SECONDS

    # remove old requests
    _requests[ip] = [
        t for t in _requests[ip] if t > window_start
    ]

    if len(_requests[ip]) >= AI_LIMIT:
        return False

    _requests[ip].append(now)
    return True
