from pydantic import BaseModel
from typing import Optional, Dict, Any

class ChatMemory(BaseModel):
    lastCrop: Optional[str] = None
    lastIntent: Optional[str] = None
    lastDistrict: Optional[str] = None
    lastState: Optional[str] = None
    lastMandi: Optional[str] = None


class ChatRequest(BaseModel):
    message: str
    language: str
    location: Optional[Dict[str, Any]] = None
    memory: Optional[ChatMemory] = None
    aiEnabled: bool = False


class ChatResponse(BaseModel):
    text: str
    priceData: Optional[Dict[str, Any]] = None
    confidence: Optional[str] = None
    memory: Optional[ChatMemory] = None
