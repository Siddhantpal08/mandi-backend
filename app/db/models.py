from sqlalchemy import Column, Integer, String, Date, Text, DateTime
from app.db.database import Base
from datetime import datetime


class MandiPrice(Base):
    __tablename__ = "mandi_prices"

    id = Column(Integer, primary_key=True, index=True)
    crop = Column(String)
    mandi = Column(String)
    district = Column(String)
    state = Column(String)
    min_price = Column(Integer)
    max_price = Column(Integer)
    modal_price = Column(Integer)
    date = Column(Date)
    source = Column(String)


class AIExplanationLog(Base):
    __tablename__ = "ai_explanation_logs"

    id = Column(Integer, primary_key=True, index=True)
    crop = Column(String, index=True)
    mandi = Column(String)
    language = Column(String(5))
    explanation = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
