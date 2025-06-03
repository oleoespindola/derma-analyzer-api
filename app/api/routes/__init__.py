from fastapi import APIRouter
from . import user, token, keras_model

router = APIRouter()
router.include_router(user.router)
router.include_router(token.router)
router.include_router(keras_model.router)
