from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends
from jwt.exceptions import InvalidTokenError

from app.security import oauth2_scheme
from app.settings import settings
from app.users.schemas import TokenData, User, UserInDB
from app.users.dao import UserDAO
from app.exceptions import credentials_exception, inactive_user_exception


ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(password: str, hashed_password: str):
    return UserDAO.is_valid_password(password, hashed_password)


def authenticate_user(username: str, password: str) -> UserInDB | None:
    user = get_user(username)
    if user and verify_password(password, user.hashed_password):
        return user


def create_access_token(
    sub: str | int,  # sub это индентификатор пользователя
    data: dict = {}, 
    expires_delta: timedelta | None = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
) -> str:
    to_encode = {
        'sub': sub,
        'exp': datetime.now(timezone.utc) + expires_delta
    }
    to_encode.update(data)
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def get_user(username: str) -> UserInDB | None:
    return UserDAO.find_one_or_none(username=username)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        username = payload.get('sub')

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise inactive_user_exception
    return current_user

