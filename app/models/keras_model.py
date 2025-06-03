import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
def get_keras_model():
    return tf.keras.models.load_model('app/models/model.keras')

def predict_image(image_array):
    model = get_keras_model()
    prediction = model.predict(image_array)[0][0]
    return prediction
