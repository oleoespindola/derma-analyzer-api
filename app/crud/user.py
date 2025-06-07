from datetime import datetime
from typing import Any
from fastapi import HTTPException

from sqlalchemy.orm import Session

import cloudinary
import cloudinary.uploader

from app.models.user import User, Image_Analysis
from app.schemas.user import UserCreate, AuthRequest
from app.core import security, auth
from app.core.config import settings
from app.keras.keras_model import predict_image
    
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.email == id).first()

def new_user(db: Session, user: UserCreate):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user: # Checks if the email is already registered
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(
        name=user.name,
        email=user.email,
        password=security.hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = auth.create_token(str(db_user.id))
    return db_user, token

def user_auth(db: Session, user: AuthRequest):
    
    db_user = get_user_by_email(db=db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Email not found")
    security.verify_password(plain_password=user.password, hashed_password=db_user.password)
    token = auth.create_token(str(db_user.id))
    return db_user, token


def prediction(
        db: Session, 
        user_id: int, 
        contents: Any,  
    ):
    predict = predict_image(contents=contents)    
    
    public_id = f"{user_id} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    try:
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_NAME,
            api_key=settings.CLOUDINARY_API,
            api_secret=settings.CLOUDINARY_API_KEY
        )    
        response = cloudinary.uploader.upload(contents, public_id=public_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Image upload erros: {str(e)}')

    try:
        image_Analysis = Image_Analysis(
            user_id=user_id,
            image_predict=predict,
            image_url=f'{public_id}; {response["secure_url"]}'
        )
        db.add(image_Analysis)
        db.commit()
        db.refresh(image_Analysis)
    except:
        cloudinary.uploader.destroy(public_id)
        raise HTTPException(status_code=500, detail="Error saving image data analysis (DB)")
    
    return predict