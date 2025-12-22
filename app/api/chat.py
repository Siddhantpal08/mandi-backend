from fastapi import APIRouter, Depends
from app.middleware.security import verify_api_key
from app.models.chat import ChatRequest, ChatResponse, ChatMemory
from app.services.chat_engine import handle_chat

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    _: str = Depends(verify_api_key)
):
    result = handle_chat(
        message=payload.message,
        memory=payload.memory.dict() if payload.memory else {},
        language=payload.language,
        location=payload.location,
        ai_enabled=payload.aiEnabled
    )

    # ✅ convert dict → ChatMemory
    if result.get("memory"):
        result["memory"] = ChatMemory(**result["memory"])

    return result
