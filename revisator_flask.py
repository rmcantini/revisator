import io
from flask import Flask, render_template, request

# Import EasyOCR
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'pt'], gpu=True)

app = Flask(__name__)

# Create a route for text extraction


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Check if a file was uploaded
    if 'image' not in request.files:
        return "No image provided."

    image = request.files['image']
    if image.filename == '':
        return "No image selected."

    # Convert the file to bytes
    image_bytes = image.read()

    # Perform text extraction on the uploaded image
    results = reader.readtext(image_bytes)

    # Process the results and create a text string
    extracted_text = ' '.join(result[1] + ' ' for result in results)

    return render_template('result.html', extracted_text=extracted_text)


if __name__ == '__main__':
    app.run()
