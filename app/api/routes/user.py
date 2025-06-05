from datetime import datetime
import os

from fastapi import APIRouter, Depends, File, HTTPException, Header, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.crud import user as user_crud
from app.models.keras_model import predict_image
from app.schemas import user as user_schemas
from app.core.auth import verify_token
from app.core.config import settings

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

os.makedirs("app/db/images", exist_ok=True)

def verify_api_key(api_key: str):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

def get_db():
    db = SessionLocal()
    try:
        yield db # Provides the session to the route
    finally:
        db.close()


@router.post("/new")
def create_user(
        user: user_schemas.UserCreate, # User data (validated by Pydantic)
        api_key: str = Header(...),
        db: Session = Depends(get_db), # Database session (injected)registered
    ):
    verify_api_key(api_key)     
    db_user, token = user_crud.new_user(db=db, user=user)
    return user_schemas.UserResponse(
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        access_token=token
    )


@router.post("/auth", response_model=user_schemas.UserResponse)
def login(
        auth_request: user_schemas.AuthRequest, # User data (validated by Pydantic)
        api_key: str = Header(...),
        db: Session = Depends(get_db), # Database session (injected)
    ):
    verify_api_key(api_key=api_key)
    db_user, token = user_crud.user_auth(db=db, user=auth_request)
    return user_schemas.UserResponse(
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        access_token=token
    )

@router.post("/predict", response_model=user_schemas.UserResponse)
async def user_predict(
        user_auth: user_schemas.UserResponse,
        db: Session = Depends(get_db),
        file: UploadFile = File(...),
        payload: dict = Depends(verify_token)
    ):
    contents = await file.read()
    prediction = predict_image(contents)
    image_url = f"app/db/images/{user_auth.id} - {datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png"
    with open(image_url, "wb") as buffer:
        buffer.write(contents)
    image_Analysis = user_crud.save_prediction(
        db=db, 
        id=user_auth.id, 
        analysis_result=prediction, 
        image_url=image_url
    )
    return JSONResponse(image_Analysis)