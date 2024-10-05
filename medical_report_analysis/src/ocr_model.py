from easyocr import Reader
import setting

class OCR:
    def __init__(self):
        pass

    def extract_text(image):
        try:
            ocr = Reader(lang_list=[setting.OCR_MODEL_LANGUAGE])
            result = ocr.readtext(image)
            text = [bbox[1] for bbox in result]
            text = "\n".join(text)
            return text
        except Exception as e:
            print(e)
