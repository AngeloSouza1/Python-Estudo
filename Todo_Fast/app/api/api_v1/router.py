from fastapi import APIRouter
from app.api.api_v1.handlers import user, task
from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(
    user.user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

router.include_router(
    task.task_router,
    prefix='/task',
    tags=['task']
)