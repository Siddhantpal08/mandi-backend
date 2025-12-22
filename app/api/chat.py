from fastapi import APIRouter, Depends
from app.middleware.security import verify_api_key
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_engine import handle_chat

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    _: str = Depends(verify_api_key)
):
    return handle_chat(
        message=payload.message,
        memory=payload.memory.dict() if payload.memory else {},
        language=payload.language,
        location=payload.location,
        ai_enabled=payload.aiEnabled
    )
