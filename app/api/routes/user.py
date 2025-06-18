import io

from fastapi import APIRouter, Depends, File, HTTPException, Header, UploadFile
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.utils import user as user_utils
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

    response = user_utils.new_user(db=db, user=user)

    return user_schemas.UserResponse(
        sub=response['user'].id,
        name=response['user'].name,
        email=response['user'].email,
        access_token=response['token']
    )

@router.post("/auth", response_model=user_schemas.UserResponse)
def login(
        auth_request: user_schemas.AuthRequest, # User data (validated by Pydantic)
        api_key: str = Header(...),
        db: Session = Depends(get_db), # Database session (injected)
    ):
    verify_api_key(api_key=api_key)

    response = user_utils.user_auth(db=db, user=auth_request)

    return user_schemas.UserResponse(
        sub=response['user'].id,
        name=response['user'].name,
        email=response['user'].email,
        access_token=response['token']
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
    
    try:
        contents = await file.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Image upload erros: {str(e)}')
    
    response = user_utils.prediction(
        db=db,
        user_id=payload['sub'],
        contents=contents
    )
    
    return JSONResponse(content={
        "predict": str(response['predict']),
        "image_id": str(response['image_id']),
        "analysis_id": str(response['analysis_id'])
    })
    
@router.post("/feedback")
def set_prediction_feedback(
        feedbackRequest: user_schemas.FeedbackRequest,
        api_key: str = Header(...),
        db: Session = Depends(get_db),
        payload: dict = Depends(verify_token)
    ):
    verify_api_key(api_key)   
    
    if not bool(feedbackRequest.feedback):
        return JSONResponse(content={"message": "Invalid feedback"}, status_code=400)
    user_utils.prediction_feedback(db=db, analysis_id=feedbackRequest.analysis_id, feedback=feedbackRequest.feedback)
    
    return JSONResponse(content={"message": "Feedback saved"})

@router.post("/history")
def get_prediction_history(
        api_key: str = Header(...),
        db: Session = Depends(get_db),
        payload: dict = Depends(verify_token)
    ):
    verify_api_key(api_key)   
    return user_utils.get_predictions_history(db=db, user_id=payload['sub'])