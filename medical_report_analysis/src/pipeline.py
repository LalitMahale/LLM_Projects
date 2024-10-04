import os
import google.generativeai as genai
from . import setting
from dotenv import load_dotenv
load_dotenv()

class LLM:
    def __init__(self):
        self.API_KEY = os.getenv("GOOGLE_API_KEY")

    def gemini_vision_llm(self,input_data:list):
        try:
            genai.configure(api_key = self.API_KEY)
            model = genai.GenerativeModel(model_name=setting.MODEL_NAME)
            response = model.generate_content(input_data)
            return response.text
        except Exception as e:
            print(e)

