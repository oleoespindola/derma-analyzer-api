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
    contents = await file.read()
    prediction = predict_image(contents)
    return JSONResponse(content={'prediction': f'{round(prediction * 100, 2)}%'})
