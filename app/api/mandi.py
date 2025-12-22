from fastapi import APIRouter
from app.services.mandi_service import MANDI_DATA

router = APIRouter()

@router.get("/")
def list_mandis():
    return MANDI_DATA
