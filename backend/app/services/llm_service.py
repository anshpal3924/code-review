# LLM service
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.interfaces.llm_interface import LLMInterface

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLMInterface):

    def __init__(self):
        # Using v1 API models (not v1beta) for better stability
        # Note: The SDK automatically prepends "models/" to model names
        model_names = [
            "gemini-2.0-flash-exp",
            "gemini-exp-1206", 
            "gemini-1.5-flash-8b",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ]
        
        self.model = None
        self.working_model_name = None
        
        for model_name in model_names:
            try:
                print(f"🔄 Trying model: {model_name}")
                test_model = genai.GenerativeModel(model_name)
                # Actually test content generation to verify it works
                test_response = test_model.generate_content("Hi", 
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        max_output_tokens=2048,
                    ))
                if test_response and test_response.text:
                    self.model = test_model
                    self.working_model_name = model_name
                    print(f"✅ Successfully initialized and tested: {model_name}")
                    return
            except Exception as e:
                error_msg = str(e)
                print(f"❌ Failed {model_name}: {error_msg[:200]}")
                continue
        
        raise Exception("No working Gemini model found. Please check API key and internet connection.")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=2048,
                ))
            return response.text
        except Exception as e:
            # If generation fails, raise with helpful context
            raise Exception(f"Content generation failed with {self.working_model_name}: {str(e)}")