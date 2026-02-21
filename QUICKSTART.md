# Quick Start Guide

## 🚀 Start the Server

```powershell
cd C:\Users\asus\OneDrive\Desktop\codebase-review\backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

## 🌐 Access Points

- **Web UI**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Status**: http://127.0.0.1:8000/status

## 🧪 Test the System

### Via Web UI (Easiest)
1. Open http://127.0.0.1:8000
2. Click "Choose File" and upload a code file
3. Click "Upload & Index"
4. Type a question in the text box
5. Click "Ask" to get answer with references

### Via Swagger UI
1. Open http://127.0.0.1:8000/docs
2. Try POST `/upload/upload` - upload a file
3. Try POST `/qa/ask` - ask a question
4. Try GET `/qa/history` - view history

### Via curl (PowerShell)

**Upload File**:
```powershell
curl -X POST http://127.0.0.1:8000/upload/upload -F "file=@yourfile.cpp"
```

**Ask Question**:
```powershell
curl -X POST http://127.0.0.1:8000/qa/ask -H "Content-Type: application/json" -d '{\"question\": \"What is this code about?\"}'
```

**View History**:
```powershell
curl http://127.0.0.1:8000/qa/history
```

**Check Status**:
```powershell
curl http://127.0.0.1:8000/status
```

## 📋 What's New

### ✅ Improvements Completed

1. **Better Code References**
   - Now shows file path and line numbers
   - Example: `auth.py (Lines 10-40)`

2. **Q&A History**
   - Last 10 questions and answers saved
   - View at `/qa/history`

3. **Status Page**
   - Shows vector store size
   - LLM connection status
   - Embedding dimension

4. **Web UI**
   - Simple interface for testing
   - Upload, ask, view history all in one page

5. **Complete Documentation**
   - README.md - Full project guide
   - AI_NOTES.md - AI usage transparency
   - PROMPTS_USED.md - Development prompts
   - ABOUTME.md - Developer info (fill in your details)
   - PROJECT_SUMMARY.md - Complete overview

## 🎯 Expected Response Format

```json
{
  "answer": "This file implements the Liskov Substitution Principle...",
  "references": [
    {
      "file_path": "liskov-subs-principle.cpp",
      "start_line": 1,
      "end_line": 50,
      "content": "// actual code content here..."
    }
  ]
}
```

## 🐛 Troubleshooting

**Server won't start?**
- Check if port 8000 is free
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

**Upload fails?**
- Check file encoding (UTF-8 preferred)
- Ensure file is text-based

**Q&A returns error?**
- Check Gemini API key in `.env`
- Ensure file was uploaded first
- Check terminal for detailed errors

**No references showing?**
- Upload a file first
- Ensure file was indexed successfully
- Check status page for vector store count

## 📝 Notes

- Server auto-reloads on code changes
- Vector store persists to disk
- History clears on server restart
- Gemini API has free tier limits

## 🎉 You're Ready!

The system is fully functional with all requested features implemented!
