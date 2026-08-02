from pathlib import Path

import pytesseract

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Exists:", Path(TESSERACT_PATH).exists())

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

print("Command:", pytesseract.pytesseract.tesseract_cmd)

print("Version:")
print(pytesseract.get_tesseract_version())