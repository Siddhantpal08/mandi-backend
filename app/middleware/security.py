# app/middleware/security.py
from fastapi import Request, HTTPException
from app.config import API_KEY

async def verify_api_key(request: Request):
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
