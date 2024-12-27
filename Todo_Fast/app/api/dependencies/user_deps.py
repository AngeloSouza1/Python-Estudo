from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.models.user_model import User
from jose import jwt
from app.core.config import settings

oauth_reusavel = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT'
)

async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        # token data
    except: 
        pass