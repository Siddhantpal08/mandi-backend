import json
from pathlib import Path
from app.db.database import engine, SessionLocal
from app.db.models import Base, MandiPrice


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    count = db.query(MandiPrice).count()

    if count == 0:
        # Correct path to JSON file
        data_path = Path(__file__).resolve().parent.parent / "data" / "mandi_sample_data.json"

        with open(data_path, "r", encoding="utf-8") as f:
            mandi_data = json.load(f)

        for item in mandi_data:
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
        print("✅ Mandi sample data seeded")

    db.close()
