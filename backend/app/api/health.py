# Health check endpoints
from fastapi import APIRouter
from app.db.database import SessionLocal
from app.core.config import settings
import openai

router = APIRouter()

@router.get("/")
def health_check():
    status = {"backend": "ok"}

    # DB check
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        status["database"] = "ok"
    except:
        status["database"] = "error"

    # LLM check
    try:
        openai.api_key = settings.OPENAI_API_KEY
        openai.models.list()
        status["llm"] = "ok"
    except:
        status["llm"] = "error"

    return status
