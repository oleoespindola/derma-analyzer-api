import io

from fastapi import APIRouter, Depends, File, HTTPException, Header, UploadFile
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.crud import user as user_crud
from app.schemas import user as user_schemas
from app.core.auth import verify_token
from app.core.config import settings

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db # Provides the session to the route
    finally:
        db.close()

def verify_api_key(api_key: str):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@router.post("/new")
def create_user( 
        user: user_schemas.UserCreate, # User data (validated by Pydantic)
        api_key: str = Header(...),
        db: Session = Depends(get_db), # Database session (injected)registered
    ):
    verify_api_key(api_key)     
    db_user, token = user_crud.new_user(db=db, user=user)
    return user_schemas.UserResponse(
        sub=db_user.id,
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
        sub=db_user.id,
        name=db_user.name,
        email=db_user.email,
        access_token=token
    )

@router.get("/current", response_model=user_schemas.UserResponse)
def get_current_user(
        api_key: str = Header(...),
        payload: dict = Depends(verify_token)
    ):
    verify_api_key(api_key)   
    return JSONResponse(payload)

@router.post("/predict", response_model=user_schemas.UserResponse)
async def user_predict(
        api_key: str = Header(...),
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        payload: dict = Depends(verify_token)
    ):
    verify_api_key(api_key)   
    
    contents = await file.read()
    predict = user_crud.prediction(
        db=db,
        user_id=payload['sub'],
        contents=contents
    )
    
    return JSONResponse(content={
        "predict": str(predict)
    })