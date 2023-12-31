import gradio as gr
import pytesseract
# import cv2


# windows install
PATH = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = PATH + r"\tesseract.exe"


def ocr(input_image):
   # image = cv2.imread(input_image, 1)
    text = pytesseract.image_to_string(input_image, lang="por")
    return text


demo = gr.Interface(
    fn=ocr,
    inputs=gr.Image(type="pil"),
    outputs="text",
)

demo.launch(share=False)
