from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.repositories.vector_store import VectorStore

class IndexingService:

    def __init__(self):
        self.chunking_service = ChunkingService()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def index_text(self, text: str):

        chunks = self.chunking_service.chunk_text(text)

        for chunk in chunks:
            embedding = self.embedding_service.generate(chunk)
            self.vector_store.store(embedding, chunk)

        self.vector_store.save()

    def index_file(self, file_path: str, text: str):
        """
        Index a file with line number tracking.
        """
        chunks = self.chunking_service.chunk_file(file_path, text)

        for chunk in chunks:
            embedding = self.embedding_service.generate(chunk["content"])
            self.vector_store.store(embedding, chunk)

        self.vector_store.save()

