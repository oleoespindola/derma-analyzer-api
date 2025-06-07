import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
import io
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

from PIL import Image

model = tf.keras.models.load_model('app/keras/model.keras')

def process_image(image):
    image = Image.open(io.BytesIO(image)).convert("RGB")
    image = image.resize((224,224))
    image_array = np.array(image) / 255.5
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def predict_image(contents):
    image_array = process_image(contents)
    prediction = model.predict(image_array)[0][0]
    prediction = Decimal(str(prediction)).quantize(Decimal('1.0000000000'), rounding=ROUND_HALF_UP)
    return prediction
