# Prompts Used During Development

This document lists the key prompts used while developing this project with AI assistance.

## Initial Setup

1. **"How to run this project from terminal"**
   - Context: Starting the FastAPI project
   - Response: Instructions for virtual environment activation and uvicorn

2. **"Create complete backend folder structure following LLD principles"**
   - Context: Project scaffolding
   - Response: Created app/api/, app/services/, app/models/, app/db/, app/repositories/, app/utils/, app/core/

## Architecture & Design

3. **"Implement layered architecture with dependency injection"**
   - Context: Structuring services and repositories
   - Response: Service layer, repository layer, and interface patterns

4. **"How to implement SOLID principles in FastAPI backend"**
   - Context: Code organization
   - Response: Single responsibility, dependency inversion examples

## OpenAI Issues

5. **"OpenAI API quota exceeded error 429"**
   - Context: File upload failing
   - Response: Suggestions to add credits or switch to alternative

6. **"Switch from OpenAI to Google Gemini API"**
   - Context: Avoiding quota issues
   - Response: Implementation of GeminiLLM class

## Gemini Integration

7. **"Google Gemini embedding model not found - models/embedding-001"**
   - Context: 404 error from Gemini API
   - Response: Try different model names

8. **"Implement hash-based embeddings as fallback"**
   - Context: Gemini embeddings not working
   - Response: SHA256 + numpy random seeding solution

9. **"List all available Gemini models and auto-select one"**
   - Context: Model discovery
   - Response: genai.list_models() with fallback logic

## Vector Store

10. **"FAISS dimension mismatch - expected 1536 but got 768"**
    - Context: Vector store error
    - Response: Update dimension in VectorStore initialization

11. **"Implement singleton pattern for VectorStore"**
    - Context: Share vector store across services
    - Response: Python singleton implementation

## File Processing

12. **"Handle different file encodings (UTF-8, Latin-1)"**
    - Context: File upload decoding errors
    - Response: Try/except with encoding fallback

13. **"Chunk code by lines preserving file path and line numbers"**
    - Context: Better code references
    - Response: Line-based chunking with metadata

## Q&A System

14. **"Q&A endpoint returning 500 error - add error logging"**
    - Context: Debugging Q&A failures
    - Response: HTTPException with traceback

15. **"Return answer with source references (file_path, line numbers)"**
    - Context: Adding proof to answers
    - Response: Modified QAService to return references dict

## History & Status

16. **"Implement last 10 Q&A history storage"**
    - Context: Track user queries
    - Response: HistoryStore singleton with list

17. **"Create status endpoint to check vector store and LLM"**
    - Context: System monitoring
    - Response: /status endpoint with component checks

## UI Development

18. **"Create simple HTML UI for file upload and Q&A"**
    - Context: Frontend interface
    - Response: Single-page HTML with fetch API

19. **"Add references display showing file path and line numbers"**
    - Context: Show proof in UI
    - Response: JavaScript to render references from API response

## Documentation

20. **"Create README with architecture diagram, flow, and how to run"**
    - Context: Project documentation
    - Response: Comprehensive README with ASCII diagrams

21. **"Document AI usage and manual verification"**
    - Context: AI transparency requirement
    - Response: AI_NOTES.md structure

22. **"Create ABOUTME.md template"**
    - Context: Developer information
    - Response: Professional profile template

## Error Handling

23. **"Add proper error handling with HTTPException in all endpoints"**
    - Context: Production-ready error responses
    - Response: Try/except blocks with status codes

24. **"Log errors with traceback for debugging"**
    - Context: Troubleshooting
    - Response: traceback.format_exc() in error handlers

## Deployment Preparation

25. **"What are the limitations of this system?"**
    - Context: Documentation honesty
    - Response: Listed embedding quality, API limits, storage issues

26. **"Suggest future enhancements for production"**
    - Context: Roadmap planning
    - Response: GitHub integration, auth, proper embeddings, etc.

---

## Prompt Engineering Insights

### Effective Prompts
- ✅ Specific technical requirements (e.g., "FAISS with dimension 768")
- ✅ Context about current errors (e.g., "404 models/gemini-pro not found")
- ✅ Constraints mentioned (e.g., "free tier only, no API quota")

### Less Effective Prompts
- ❌ Vague requests without context
- ❌ Asking for complete solutions without understanding
- ❌ Not providing error messages or logs

### Best Practices
1. Always provide error messages in full
2. Mention constraints (budget, API limits, etc.)
3. Ask for explanations, not just code
4. Verify and test AI-generated code
5. Iterate based on real testing results

---

*This document demonstrates transparency about AI usage and helps others understand the development process.*
