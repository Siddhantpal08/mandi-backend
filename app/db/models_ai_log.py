from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base

class AIExplanationLog(Base):
    __tablename__ = "ai_explanations"

    id = Column(Integer, primary_key=True)
    crop = Column(String)
    mandi = Column(String)
    language = Column(String)
    ip = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
