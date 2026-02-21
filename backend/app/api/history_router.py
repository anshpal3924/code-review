from fastapi import APIRouter
from app.repositories.history_store import HistoryStore

router = APIRouter()
history_store = HistoryStore()

@router.get("/history")
async def get_history():
    """Get last 10 Q&A pairs."""
    return {"history": history_store.get()}

@router.delete("/history")
async def clear_history():
    """Clear Q&A history."""
    history_store.clear()
    return {"message": "History cleared"}
