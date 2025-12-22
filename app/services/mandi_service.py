from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import MandiPrice

def get_price_by_crop(crop: str, location: dict | None):
    db: Session = SessionLocal()

    query = db.query(MandiPrice).filter(
        MandiPrice.crop == crop.lower()
    )

    if location:
        if location.get("state"):
            query = query.filter(
                MandiPrice.state == location["state"]
            )
        if location.get("district"):
            query = query.filter(
                MandiPrice.district == location["district"]
            )

    result = query.order_by(
        MandiPrice.modal_price.desc()
    ).first()

    db.close()

    if not result:
        return None

    return {
        "crop": result.crop,
        "mandi": result.mandi,
        "district": result.district,
        "state": result.state,
        "minPrice": result.min_price,
        "maxPrice": result.max_price,
        "modalPrice": result.modal_price,
        "date": str(result.date),
        "source": result.source
    }
