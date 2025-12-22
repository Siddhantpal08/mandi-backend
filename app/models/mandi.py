from pydantic import BaseModel

class MandiPrice(BaseModel):
    crop: str
    mandi: str
    district: str
    state: str
    minPrice: int
    maxPrice: int
    modalPrice: int
    date: str
    unit: str
    source: str
