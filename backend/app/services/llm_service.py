# LLM service
import os
from dotenv import load_dotenv
import requests
from app.interfaces.llm_interface import LLMInterface

load_dotenv()

class GeminiLLM(LLMInterface):

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise Exception("GEMINI_API_KEY not found in environment variables")
        
        # Try multiple model variations with v1 API (more stable than v1beta)
        model_attempts = [
            ("gemini-pro", "v1"),
            ("gemini-1.5-flash", "v1"),
            ("gemini-1.5-pro", "v1"),
            ("gemini-pro", "v1beta"),
        ]
        
        for model_name, api_version in model_attempts:
            try:
                print(f"🔄 Testing {model_name} with {api_version} API")
                self.model_name = model_name
                self.api_url = f"https://generativelanguage.googleapis.com/{api_version}/models/{model_name}:generateContent?key={self.api_key}"
                
                test_response = self._make_request("Hi")
                if test_response:
                    print(f"✅ Successfully initialized: {model_name} ({api_version})")
                    return
            except Exception as e:
                print(f"❌ Failed {model_name} ({api_version}): {str(e)[:150]}")
                continue
        
        raise Exception("No working Gemini model found. Check API key at https://aistudio.google.com/app/apikey")
    
    def _make_request(self, prompt: str) -> str:
        """Make a direct HTTP request to Gemini API"""
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 2048,
            }
        }
        
        response = requests.post(
            self.api_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code != 200:
            raise Exception(f"API returned {response.status_code}: {response.text}")
        
        result = response.json()
        
        if "candidates" in result and len(result["candidates"]) > 0:
            candidate = result["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                return candidate["content"]["parts"][0]["text"]
        
        raise Exception(f"Unexpected API response format: {result}")

    def generate(self, prompt: str) -> str:
        try:
            return self._make_request(prompt)
        except Exception as e:
            raise Exception(f"Content generation failed: {str(e)}")