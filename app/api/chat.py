from fastapi import APIRouter, Depends, Request, HTTPException
from app.middleware.security import verify_api_key
from app.security.rate_limiter import allow_ai_request
from app.models.chat import ChatRequest, ChatResponse, ChatMemory
from app.services.chat_engine import handle_chat

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    request: Request,
    _: str = Depends(verify_api_key)
):
    if payload.aiEnabled:
        ip = request.client.host
        if not allow_ai_request(ip):
            raise HTTPException(
                status_code=429,
                detail="AI usage limit reached. Try later."
            )

    result = handle_chat(
        message=payload.message,
        memory=payload.memory.dict() if payload.memory else {},
        language=payload.language,
        location=payload.location,
        ai_enabled=payload.aiEnabled
    )

    if result.get("memory"):
        result["memory"] = ChatMemory(**result["memory"])

    return result
