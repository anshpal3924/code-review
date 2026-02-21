from app.services.embedding_service import EmbeddingService
from app.repositories.vector_store import VectorStore

class RetrievalService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()  # singleton

    def retrieve(self, question: str):
        """
        Retrieve relevant chunks with full metadata (file_path, lines, content).
        """
        embedding = self.embedding_service.generate(question)
        results = self.vector_store.search(embedding)
        return results  # Returns list of dicts with metadata
