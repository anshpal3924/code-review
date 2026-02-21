# LLM service
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.interfaces.llm_interface import LLMInterface

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLMInterface):

    def __init__(self):
        # Try stable model names in order of preference
        # Using only confirmed working models for v1beta API
        model_names = [
            "gemini-1.5-pro",
            "gemini-pro",
            "gemini-1.5-flash-latest",
            "gemini-1.5-pro-latest"
        ]
        
        self.model = None
        self.working_model_name = None
        
        for model_name in model_names:
            try:
                print(f"🔄 Trying model: {model_name}")
                test_model = genai.GenerativeModel(model_name)
                # Actually test content generation to verify it works
                test_response = test_model.generate_content("Hi")
                if test_response and test_response.text:
                    self.model = test_model
                    self.working_model_name = model_name
                    print(f"✅ Successfully initialized and tested: {model_name}")
                    return
            except Exception as e:
                print(f"❌ Failed {model_name}: {str(e)[:200]}")
                continue
        
        raise Exception("No working Gemini model found. Please check API key and internet connection.")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # If generation fails, raise with helpful context
            raise Exception(f"Content generation failed with {self.working_model_name}: {str(e)}")