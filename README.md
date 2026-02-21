# Codebase Q&A System with Proof

A FastAPI-based intelligent code question-answering system that provides answers with source references (proof).

## 🚀 Features

- **File Upload & Indexing**: Upload code files and automatically chunk & index them
- **Intelligent Q&A**: Ask questions about your codebase and get AI-powered answers
- **Source References**: Every answer includes references to specific files and line numbers (proof)
- **Q&A History**: View last 10 question-answer pairs
- **Simple Web UI**: Built-in HTML interface for easy interaction
- **Vector Search**: FAISS-based similarity search for relevant code retrieval
- **LLM Integration**: Google Gemini AI for generating answers

## 📐 Architecture

### Layered Architecture (SOLID Principles)

```
┌─────────────────────────────────────────┐
│         API Layer (FastAPI)             │
│  - upload_router.py                     │
│  - qa.py                                │
│  - history_router.py                    │
│  - status_router.py                     │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│         Service Layer                   │
│  - indexing_service.py                  │
│  - qa_service.py                        │
│  - chunking_service.py                  │
│  - embedding_service.py                 │
│  - llm_service.py                       │
│  - retrieval_service.py                 │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│       Repository Layer                  │
│  - vector_store.py (FAISS)              │
│  - history_store.py                     │
│  - database.py (SQLite)                 │
└─────────────────────────────────────────┘
```

## 🔄 Flow

### Upload Flow
```
1. User uploads file → upload_router.py
2. IndexingService.index_file(filename, content)
3. ChunkingService.chunk_file() → chunks with line numbers
4. EmbeddingService.generate() → 768-dim vectors (hash-based)
5. VectorStore.store() → FAISS index
6. VectorStore.save() → persist to disk
```

### Q&A Flow
```
1. User asks question → qa.py
2. QAService.process_query(question)
3. RetrievalService.retrieve() → search vector store
4. VectorStore.search() → top 3 similar chunks
5. GeminiLLM.generate() → answer with context
6. HistoryStore.save() → save Q&A pair
7. Return {answer, references} with file paths & line numbers
```

## 🛠️ How to Run

### Prerequisites
- Python 3.12+
- Google Gemini API Key

### Installation

1. **Clone the repository**
```bash
cd codebase-review/backend
```

2. **Create virtual environment**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./codebase_qa.db
```

5. **Run the server**
```bash
uvicorn app.main:app --reload
```

6. **Access the application**
- Web UI: http://127.0.0.1:8000
- API Docs: http://127.0.0.1:8000/docs
- Status: http://127.0.0.1:8000/status

## 📚 API Endpoints

### Upload
- `POST /upload/upload` - Upload and index a file

### Q&A
- `POST /qa/ask` - Ask a question
  - Request: `{"question": "your question"}`
  - Response: `{"answer": "...", "references": [...]}`

### History
- `GET /qa/history` - Get last 10 Q&A pairs
- `DELETE /qa/history` - Clear history

### Status
- `GET /status` - Check system status
- `GET /health` - Health check

## 🧩 Components

### Embedding Strategy
- **Hash-based embeddings**: Uses SHA256 hash + numpy random seeding
- **Dimension**: 768
- **Benefit**: Deterministic, no API quota, works offline

### LLM
- **Model**: Google Gemini 2.5 Flash
- **Auto-detection**: Automatically finds available model
- **Fallback**: Tries multiple model names

### Vector Store
- **Engine**: FAISS (IndexFlatL2)
- **Persistence**: Saves to `faiss_index.bin` and `metadata.pkl`
- **Singleton**: Single shared instance across app

### Chunking
- **Strategy**: Line-based chunking
- **Chunk size**: 50 lines per chunk
- **Metadata**: Tracks file_path, start_line, end_line

## ⚠️ Limitations

1. **Embedding Quality**: Hash-based embeddings are deterministic but not semantic
   - For production, use proper embedding models (OpenAI, Sentence Transformers)
2. **Gemini API**: Free tier has rate limits
3. **Storage**: In-memory vector store (cleared on restart unless persisted)
4. **File Types**: Text files only (code, markdown, etc.)
5. **No Authentication**: No user auth implemented
6. **Single User**: Not designed for concurrent multi-user scenarios

## 🔮 Future Enhancements

- [ ] GitHub repository cloning & indexing
- [ ] Proper semantic embeddings (Sentence Transformers)
- [ ] PostgreSQL with pgvector
- [ ] User authentication
- [ ] Multi-file upload
- [ ] Code syntax highlighting in references
- [ ] Export Q&A history to PDF
- [ ] API key management UI

## 📝 License

MIT License

## 👤 Author

See ABOUTME.md for author details.
