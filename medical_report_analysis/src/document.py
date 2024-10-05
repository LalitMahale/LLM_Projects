import fitz
import os
from PIL import Image
import setting
import json
import numpy as np


class PDF_Processing:
    def __init__(self):
        pass

    def pdf_to_image(file):
        """
        This function will take pdf file and convert first page into image and return it.

        LOCAL_TEST : True / False
        
        """

        try:
            if setting.LOCAL_TEST:
                pdf_file = fitz.open(filename=file,filetype="pdf")
            else:
                pdf_file = file.open(stream = file.read(),filetype ="pdf")
            page = pdf_file.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))  # 300 DPI
            image_bytes = pix.samples
            image = Image.frombytes("RGB", [pix.width, pix.height], image_bytes)
            image_np = np.array(image)

            return image_np
        except Exception as e:
            print(e)

    def get_clean_json(text:str):
        """
        This function will take text and ret
        """

        try:
            text = text.replace("json","").replace("```","")
            return json.loads(text)
        except Exception as e:
            print(e)