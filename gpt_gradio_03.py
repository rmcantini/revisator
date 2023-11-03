import gradio as gr
import cv2
import pytesseract
import numpy as np
import language_tool_python

# Initialize Grammarly
tool = language_tool_python.LanguageTool('pt-BR')

# Your OCR preprocessing function


def ocr_preprocess(image_pil):
    # ... (your existing code)

    extracted_text = pytesseract.image_to_string(denoised, lang="por")

    # Correct grammar and spelling using Grammarly
    corrected_text = tool.correct(extracted_text)

    return corrected_text


iface = gr.Interface(
    fn=ocr_preprocess,
    inputs="image",
    outputs="text",
    live=False,
)
iface.launch()
