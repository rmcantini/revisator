import gradio as gr
import pytesseract
import cv2


# windows install
PATH = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = PATH + r"\tesseract.exe"


def preprocess_image(input_image):
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded


def ocr(preprocessed_image):
    text = pytesseract.image_to_string(preprocessed_image, lang="por")
    return text


demo = gr.Interface(
    fn=ocr,
    inputs=gr.Image(type="pil"),
    outputs="text",
)

demo.launch(share=False)
