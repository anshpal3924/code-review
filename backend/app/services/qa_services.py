from app.services.retrieval_service import RetrievalService
from app.services.llm_service import OpenAILLM

class QAService:

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.llm = OpenAILLM()

    def process_query(self, question: str):

        context_chunks = self.retrieval_service.retrieve(question)

        context = "\n".join(context_chunks)

        prompt = f"""
        Use the following context to answer the question.

        Context:
        {context}

        Question:
        {question}
        """

        answer = self.llm.generate(prompt)
        return answer
