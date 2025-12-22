from fastapi import APIRouter, Depends
from app.middleware.auth import verify_api_key
from app.services.chat_engine import handle_chat
from app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    _: str = Depends(verify_api_key)
):
    return handle_chat(
        message=payload.message,
        memory=payload.memory,
        language=payload.language,
        location=payload.location,
        ai_enabled=payload.aiEnabled
    )
