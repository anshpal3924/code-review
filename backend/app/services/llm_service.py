# LLM service
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.interfaces.llm_interface import LLMInterface

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLMInterface):

    def __init__(self):
        # Try direct model names without listing (for deployment compatibility)
        model_names = [
            "gemini-1.5-flash",
            "gemini-1.5-pro", 
            "gemini-pro",
            "models/gemini-1.5-flash",
            "models/gemini-1.5-pro",
            "models/gemini-pro"
        ]
        
        for model_name in model_names:
            try:
                print(f"🔄 Trying model: {model_name}")
                self.model = genai.GenerativeModel(model_name)
                # Test if model works
                print(f"✅ Successfully initialized with: {model_name}")
                return
            except Exception as e:
                print(f"❌ Failed {model_name}: {str(e)[:100]}")
                continue
        
        raise Exception("No working Gemini model found. Please check API key and internet connection.")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text