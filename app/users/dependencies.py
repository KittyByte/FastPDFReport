from typing import Annotated

import jwt
from fastapi import Depends
from jwt.exceptions import InvalidTokenError

from app.security import oauth2_scheme
from app.settings import settings, ALGORITHM
from app.users.schemas import TokenData, User
from app.exceptions import credentials_exception, inactive_user_exception
from app.users.service import get_user



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


GetCurrentActiveUserDep = Annotated[User, Depends(get_current_active_user)]
GetCurrentUserDep = Annotated[User, Depends(get_current_user)]


