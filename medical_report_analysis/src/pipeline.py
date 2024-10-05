from document import PDF_Processing
from ocr_model import OCR
import prompts
from llms import LLM
import os


class Pipeline:
    def __init__(self):
        self.cwd = os.getcwd()

    def process(file):
        try:
            image = PDF_Processing.pdf_to_image(os.path.join(os.getcwd(),file))
            text = OCR.extract_text(image)
            print(text)
            json_text = LLM().get_json(input_data=text)
            print(json_text)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    path = "test_docs/WM17S.pdf"
    result = Pipeline.process(path)