from app.services.retrieval_service import RetrievalService
from app.services.llm_service import GeminiLLM
from app.repositories.history_store import HistoryStore

class QAService:

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.llm = GeminiLLM()
        self.history_store = HistoryStore()

    def process_query(self, question: str):
        # Retrieve relevant context chunks with metadata
        context_chunks = self.retrieval_service.retrieve(question)

        # Extract content for LLM prompt
        if isinstance(context_chunks, list) and len(context_chunks) > 0:
            if isinstance(context_chunks[0], dict):
                context = "\n\n".join([chunk.get("content", "") for chunk in context_chunks])
            else:
                context = "\n\n".join(context_chunks)
        else:
            context = ""

        # Create prompt
        prompt = f"""Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""

        # Generate answer
        answer = self.llm.generate(prompt)
        
        # Save to history
        self.history_store.save(question, answer)

        # Return answer with references
        return {
            "answer": answer,
            "references": context_chunks
        }

