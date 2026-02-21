# AI Usage Notes

## AI Assistance in This Project

This project was developed with assistance from AI tools (GitHub Copilot / Claude) to accelerate development and ensure best practices.

## Areas Where AI Was Used

### 1. **Architecture Design**
- AI provided guidance on layered architecture following SOLID principles
- Suggested dependency injection pattern
- Recommended repository pattern for data access
- Helped structure the project following industry standards

### 2. **Code Generation**
- Boilerplate code for FastAPI routers and services
- Initial implementation of chunking and embedding services
- Database setup with SQLAlchemy
- Error handling patterns

### 3. **Problem Solving**
- Debugging OpenAI API quota issues → Switched to Google Gemini
- Resolving Gemini embedding API compatibility → Hash-based embeddings
- PowerShell activation script issues
- Vector dimension mismatch troubleshooting

### 4. **Documentation**
- README.md structure and content
- Code comments and docstrings
- API documentation in FastAPI

## Manual Verification & Customization

### What Was Verified Manually
- ✅ All code logic reviewed and tested
- ✅ API endpoints tested via Swagger UI and curl
- ✅ File upload and encoding handling
- ✅ Q&A flow from upload to answer generation
- ✅ Vector store persistence
- ✅ Error handling and edge cases

### Custom Implementations
- **Hash-based embeddings**: Custom solution when Gemini embeddings failed
- **Line-based chunking**: Implemented to preserve file structure and line numbers
- **History store**: Simple in-memory singleton for Q&A tracking
- **HTML UI**: Built-in web interface for easy testing
- **Model auto-detection**: Gemini model discovery and fallback logic

## AI Tools Used

1. **GitHub Copilot** / **Claude Sonnet 4.5**
   - Code completion and suggestions
   - Architecture recommendations
   - Debugging assistance
   - Documentation generation

## Human Decisions

The following key decisions were made by the developer:

1. **Hash-based embeddings** instead of waiting for Gemini API fixes
2. **Line-based chunking** (50 lines) for better code context
3. **FAISS** for vector storage (simple, fast, no external dependencies)
4. **Google Gemini** over OpenAI (free tier, no quota issues)
5. **Single-page HTML UI** instead of separate React frontend
6. **Singleton patterns** for VectorStore and HistoryStore
7. **Metadata structure** for file references (file_path, start_line, end_line)

## Verification Process

Each AI-generated component was:
1. Reviewed for correctness
2. Tested with real data
3. Modified where necessary
4. Integrated with manual code
5. Documented properly

## Transparency

This document serves as full disclosure that AI assistance was used in this project, following the assignment requirement to document AI usage.

**Note**: While AI provided scaffolding and suggestions, all final decisions, testing, and verification were done manually by the developer.

---

*Last Updated: February 21, 2026*
