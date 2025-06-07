from datetime import datetime
from decimal import Decimal
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
    
def get_user_by_email(db: Session, email: str) -> Session:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: str) -> User:
    return db.query(User).filter(User.email == id).first()

def new_user(db: Session, user: UserCreate) -> dict[User, str]:

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
    
    return {
        'user': db_user,
        'token': auth.create_token(str(db_user.id))
    }

def user_auth(db: Session, user: AuthRequest) -> dict[User, str]:  

    db_user = get_user_by_email(db=db, email=user.email)

    if not db_user:
        raise HTTPException(status_code=401, detail="Email not found")

    security.verify_password(plain_password=user.password, hashed_password=db_user.password)

    return {
        'user': db_user, 
        'token': auth.create_token(str(db_user.id))
    }


def prediction(db: Session, user_id: int, contents: Any) -> dict[Decimal, int, int]:

    predict = predict_image(contents=contents)        
    image_id = f"{user_id} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    try:
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_NAME,
            api_key=settings.CLOUDINARY_API,
            api_secret=settings.CLOUDINARY_API_KEY
        )    
        response = cloudinary.uploader.upload(contents, public_id=image_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Image upload erros: {str(e)}')

    try:
        image_Analysis = Image_Analysis(
            user_id=user_id,
            image_predict=predict,
            image_url=f'{image_id}; {response["secure_url"]}'
        )
        db.add(image_Analysis)
        db.commit()
        db.refresh(image_Analysis)
    except:
        cloudinary.uploader.destroy(image_id)
        raise HTTPException(status_code=500, detail="Error saving image data analysis (DB)")
    
    return {
        'predict': predict, 
        'image_id': image_id,
        'analysis_id': image_Analysis.id
    }

def prediction_feedback(db: Session, analysis_id: int, feedback: bool) -> None:
    image_Analysis = Image_Analysis(
        id=analysis_id,
        user_feedback=feedback,
        feedback_timestamp=datetime.now()
    )
    db.merge(image_Analysis)
    db.commit()