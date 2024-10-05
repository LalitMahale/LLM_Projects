import os
import google.generativeai as genai
import setting
from dotenv import load_dotenv
from prompts import Prompts
load_dotenv()


class LLM:
    def __init__(self):
        self.API_KEY = os.getenv("GOOGLE_API_KEY")

    def get_json(self,input_data:str):
        try:
            genai.configure(api_key = self.API_KEY)
            model = genai.GenerativeModel(model_name=setting.MODEL_NAME)
            print("model loaded")
            response = model.generate_content(Prompts.text_json_prompt().format(text = input_data))
            print("problem")
            return response.text
        except Exception as e:
            print(e)

