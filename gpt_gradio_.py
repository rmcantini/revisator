import gradio as gr
from PIL import Image
import cv2
import pytesseract
import numpy as np

# windows install
PATH = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = PATH + r"\tesseract.exe"


def ocr_preprocess(image_pil, save_path=None):
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(
        gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    denoised = cv2.fastNlMeansDenoising(
        binary, None, h=30, templateWindowSize=7, searchWindowSize=21)
    coords = np.column_stack(np.where(denoised > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    rotated = Image.fromarray(denoised)
    rotated = rotated.rotate(angle, expand=1)
    rotated = np.array(rotated)
    if save_path:
        cv2.imwrite(save_path, rotated)
    extracted_text = pytesseract.image_to_string(rotated, lang="por")
    return Image.fromarray(rotated), extracted_text


iface = gr.Interface(
    fn=ocr_preprocess,
    inputs="image",
    outputs=["image", "text"],
    live=False,
)
iface.launch()
