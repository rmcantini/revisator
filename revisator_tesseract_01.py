import pytesseract
import cv2

# windows install
PATH = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = PATH + r"\tesseract.exe"

# actual code
image = cv2.imread(r"images\01.png")
text = pytesseract.image_to_string(image, lang="por")
print(text)
