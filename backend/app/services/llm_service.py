# LLM service
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.interfaces.llm_interface import LLMInterface

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLMInterface):

    def __init__(self):
        # List available models and pick the first generative one
        print("🔍 Listing available Gemini models...")
        try:
            for model in genai.list_models():
                if 'generateContent' in model.supported_generation_methods:
                    print(f"✅ Available model: {model.name}")
                    # Use the first available model
                    self.model = genai.GenerativeModel(model.name)
                    print(f"✅ Using model: {model.name}")
                    return
        except Exception as e:
            print(f"⚠️ Could not list models: {e}")
        
        # Fallback to common model names
        for model_name in ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-pro"]:
            try:
                print(f"🔄 Trying model: {model_name}")
                self.model = genai.GenerativeModel(model_name)
                print(f"✅ Successfully initialized with: {model_name}")
                return
            except Exception as e:
                print(f"❌ Failed {model_name}: {e}")
                continue
        
        raise Exception("No working Gemini model found")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text