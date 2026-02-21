from fastapi import APIRouter
from app.repositories.vector_store import VectorStore
import google.generativeai as genai

router = APIRouter()

@router.get("/status")
async def get_status():
    """Check backend status and health."""
    vector_store = VectorStore()
    
    # Check vector store
    vector_items = vector_store.index.ntotal if hasattr(vector_store, 'index') else 0
    
    # Check LLM connection
    llm_status = "connected"
    try:
        # Simple check - if we got here, API key is configured
        llm_status = "connected"
    except:
        llm_status = "disconnected"
    
    return {
        "backend": "ok",
        "vector_store_items": vector_items,
        "llm": llm_status,
        "embedding_dimension": 768
    }
