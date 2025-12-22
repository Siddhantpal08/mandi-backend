import json
from datetime import datetime
from app.db.database import SessionLocal
from app.db.models import MandiPrice

DATA_PATH = "app/data/mandi_sample_data.json"

db = SessionLocal()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    mandi_data = json.load(f)

count = 0

for row in mandi_data:
    record = MandiPrice(
        crop=row["crop"].lower(),
        mandi=row["mandi"],
        district=row["district"],
        state=row["state"],
        min_price=row["minPrice"],
        max_price=row["maxPrice"],
        modal_price=row["modalPrice"],
        date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
        source=row["source"]
    )
    db.add(record)
    count += 1

db.commit()
db.close()

print(f"{count} mandi records imported successfully")
