from app.db.database import engine, SessionLocal
from app.db.models import Base, MandiPrice
from app.data.mandiSampleData import MANDI_DATA

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    count = db.query(MandiPrice).count()

    if count == 0:
        for item in MANDI_DATA:
            db.add(MandiPrice(
                crop=item["crop"].lower(),
                mandi=item["mandi"],
                district=item["district"],
                state=item["state"],
                min_price=item["minPrice"],
                max_price=item["maxPrice"],
                modal_price=item["modalPrice"],
                date=item["date"],
                source=item["source"]
            ))
        db.commit()

    db.close()
