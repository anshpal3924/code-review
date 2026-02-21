from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.indexing_service import IndexingService
import traceback

router = APIRouter()
indexing_service = IndexingService()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        
        # Try different encodings
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = content.decode("latin-1")
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Unable to decode file: {str(e)}")

        # Index file with filename
        indexing_service.index_file(file.filename, text)

        return {"message": "File indexed successfully", "filename": file.filename}
    
    except HTTPException:
        raise
    except Exception as e:
        error_msg = str(e)
        print(f"❌ ERROR in upload: {error_msg}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=error_msg)
