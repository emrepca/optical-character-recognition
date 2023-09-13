import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open('image/deneme.png')
text = pytesseract.image_to_string(img, lang = "tur")

print(text)