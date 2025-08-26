from datetime import datetime, timedelta, timezone

import jwt

from app.settings import settings, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.users.schemas import UserInDB
from app.users.dao import UserDAO



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

