from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

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
