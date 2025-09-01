from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.users.schemas import Token, User
from app.exceptions import invalid_user_exception
from app.users.service import authenticate_user, create_access_token
from app.users.dependencies import GetCurrentActiveUserDep


router = APIRouter(
    prefix='/users', tags=['User']
)


@router.post("/token")
async def create_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise invalid_user_exception
    access_token = create_access_token(sub = user.username)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=User)
async def read_users_me(current_user: GetCurrentActiveUserDep):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: GetCurrentActiveUserDep):
    return [{"item_id": "Foo", "owner": current_user.username}]

