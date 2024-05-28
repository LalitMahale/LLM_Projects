from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

class LLM:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_GEMINI_API")

    def get_llm(self,model = "gemini-pro",temperature = 0):
        llm = GoogleGenerativeAI(google_api_key=self.api_key, model = model, temperature=temperature)
        return llm

    def summerization_prompt(self,text):
        return f"""You are the expert in summarization. You have to summerize below text.\nText : {text}
        """




if __name__ == "__main__":
    llm_model = LLM()
    res = llm_model.get_llm().invoke("hi")
    out = llm_model.summerization_prompt(res)
    print(out)