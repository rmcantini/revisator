import gradio as gr
import easyocr
import tempfile
import os
from PIL import Image

# Function to process an image and extract text


def extract_text(image):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the uploaded image to a temporary file
        image_path = os.path.join(temp_dir, "uploaded_image.png")
        image.save(image_path)

        # Perform text extraction
        reader = easyocr.Reader(['en', 'pt'], gpu=True)
        results = reader.readtext(image_path)

        text = ' '.join(result[1] for result in results)
    return text


# Create a Gradio interface
iface = gr.Interface(
    fn=extract_text,
    inputs=gr.inputs.Image(type="pil", label="Upload an image"),
    outputs=gr.outputs.Textbox(label="Extracted Text")
)

iface.launch()
