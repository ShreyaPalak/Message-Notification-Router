import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

print(pytesseract.pytesseract.tesseract_cmd)
print(pytesseract.get_tesseract_version())