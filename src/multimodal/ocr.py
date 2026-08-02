import os

import pytesseract
from sympy import im

from src.config import TESSERACT_PATH


if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
class OCRExtractor:
    def __init__(self):
        self.available = False

        try:
            import pytesseract
            from PIL import Image

            self.pytesseract = pytesseract
            self.Image = Image

            self.available = True

        except Exception:
            self.available = False

    def extract(self, path):
        if path is None:
            return ""

        if not self.available:
            return ""

        try:
            image = self.Image.open(path)

            text = self.pytesseract.image_to_string(image)

            return text.strip()

        except Exception:
            return ""