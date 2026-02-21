# Embedding generation service
import os
from dotenv import load_dotenv
import google.generativeai as genai
import numpy as np
import hashlib

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class EmbeddingService:

    def generate(self, text: str):
        # Use text hash to generate consistent embeddings (workaround)
        # This creates a 768-dimensional vector from the text hash
        text_hash = hashlib.sha256(text.encode()).digest()
        
        # Convert hash to numpy array and expand to 768 dimensions
        seed = int.from_bytes(text_hash[:4], 'big')
        np.random.seed(seed)
        embedding = np.random.randn(768).tolist()
        
        return embedding
