from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np

from app.models.keras_model import predict_image

router = APIRouter(
    tags=["Keras"]
)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = await file.read()
    image = Image.open(io.BytesIO(image)).convert("RGB")
    image = image.resize((224,224))
    image_array = np.array(image) / 255.5
    image_array = np.expand_dims(image_array, axis=0)

    prediction = predict_image(image_array)
    return JSONResponse(content={'prediction': f'{round(prediction * 100, 2)}%'})
