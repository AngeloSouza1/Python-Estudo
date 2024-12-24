from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth, UserDetail
from app.services.user_service import UserService
from app.models.user_model import User
import pymongo

user_router = APIRouter()

@user_router.post('/adiciona', summary='Adiciona Usuário', response_model=UserDetail)
async def adiciona_usuario(data: UserAuth):
    # Verifique se o usuário já existe
    existing_user = await User.find_one(User.username == data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username já existe."
        )
    
    try:
        # Adiciona o usuário
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username ou e-mail deste usuário já existe."
        )
    except beanie.exceptions.RevisionIdWasChanged:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflito ao salvar o documento. Tente novamente."
        )
