from pydantic import BaseModel, Field
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: str
    exp: datetime


class User(BaseModel):
    username: str
    fullname: str | None = None
    email: str | None = None
    disabled: bool
    telegram_id: int | None = None


class UserInDB(User):
    id: int
    hashed_password: str = Field(validation_alias='password')

