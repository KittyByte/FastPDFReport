import bcrypt

from app.orm.dao import BaseDAO
from app.users.models import UserOrm
from app.users.schemas import UserInDB


class UserDAO(BaseDAO):
    model = UserOrm

    @classmethod
    def _hash_password(cls, password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    @classmethod
    def find_one_by(cls, **filter_by):
        user = super().find_one_by(**filter_by)
        return UserInDB(**user) if user else None

    @classmethod
    def create(cls, **data):
        data['password'] = cls._hash_password(data['password'])
        return super().create(**data)
    
    @classmethod
    def create_bulk(cls, values):
        for value in values:
            value['password'] = cls._hash_password(value['password'])
        return super().create_bulk(values)

    @classmethod
    def is_valid_password(cls, password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
