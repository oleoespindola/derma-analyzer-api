from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

app.include_router(router)

@router.get("/")
async def predict():
    return JSONResponse(content={
        "message": "Visit https://github.com/oleoespindola/derma-analyzer-api for documentation"
    })

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=7860, reload=True)
