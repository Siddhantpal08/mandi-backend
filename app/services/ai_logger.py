from app.db.database import SessionLocal
from app.db.models import AIExplanationLog

def log_ai_explanation(
    crop: str,
    mandi: str,
    language: str,
    explanation: str
):
    try:
        db = SessionLocal()
        log = AIExplanationLog(
            crop=crop,
            mandi=mandi,
            language=language,
            explanation=explanation
        )
        db.add(log)
        db.commit()
    except Exception:
        # Logging must NEVER break user flow
        pass
    finally:
        db.close()
