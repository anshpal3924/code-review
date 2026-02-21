from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.qa_service import QAService
import traceback

router = APIRouter()
qa_service = QAService()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(req: QuestionRequest):
    try:
        answer = qa_service.process_query(req.question)
        return {"answer": answer}
    except Exception as e:
        print(f"❌ ERROR in QA: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
