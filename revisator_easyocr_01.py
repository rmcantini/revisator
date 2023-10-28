"""Super python webapp for image checking
"""
import easyocr

reader = easyocr.Reader(['en', 'pt'], gpu=False)
results = reader.readtext('images\\01.png')

TEXT = ' '
for result in results:
    TEXT += result[1] + ' '

print(TEXT)
