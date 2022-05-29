import keras
from keras.datasets import cifar10

import numpy as np
from PIL import Image, ImageOps
import os

def save_image(filename, data_array):
    im = Image.fromarray(data_array.astype('uint8'))
    im_invert = ImageOps.invert(im)
    im_invert.save(filename)

# Load Fashion-MNIST Data
(_, _), (x_test, y_test) = cifar10.load_data()

DIR_NAME = "JPEGImagesc"
if os.path.exists(DIR_NAME) == False:
    os.mkdir(DIR_NAME)

# Save Images
i = 0
for li in [x_test]:
    print("[---------------------------------------------------------------]")
    for x in li:
        if i == 10:
            break
        filename = "{0}/{1:05d}.jpg".format(DIR_NAME,i)
        print(filename)
        save_image(filename, x)
        i += 1