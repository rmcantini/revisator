import gradio as gr
import cv2
import pytesseract
import numpy as np

# windows install
PATH = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = PATH + r"\tesseract.exe"


def ocr_preprocess(image_pil):
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(
        gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    denoised = cv2.fastNlMeansDenoising(
        binary, None, h=30, templateWindowSize=7, searchWindowSize=21)

    # Get bounding boxes of text regions
    custom_config = r'--oem 3 --psm 6'
    results = pytesseract.image_to_boxes(denoised, config=custom_config)

    for line in results.splitlines():
        b = line.split()
        if len(b) == 12:
            x, y, w, h, angle = int(b[1]), int(
                b[2]), int(b[3]), int(b[4]), float(b[6])
            if angle > 0.5:
                angle = 90 - angle
                rotated = cv2.warpAffine(denoised, cv2.getRotationMatrix2D(
                    (x, y), angle, 1.0), (denoised.shape[1], denoised.shape[0]))
                denoised = rotated

    extracted_text = pytesseract.image_to_string(denoised, lang="por")
    return extracted_text


iface = gr.Interface(
    fn=ocr_preprocess,
    inputs="image",
    outputs="text",
    live=False,
)
iface.launch()
