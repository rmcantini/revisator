"""Another ocr attempt"""


import pandas as pd
from glob import glob
import numpy as np
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
from PIL import Image
import keras_ocr


img_fns = glob("images/*.png")


pipeline = keras_ocr.pipeline.Pipeline()

results = pipeline.recognize([img_fns[0]])

keras_ocr.tools.drawAnnotations(plt.imread(img_fns[0]), results[0])
plt.show()

predicted_image = results[0]
for text, box in predicted_image:
    print(text)
