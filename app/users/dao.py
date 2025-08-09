from app.orm.dao import BaseDAO
from app.users.models import UserOrm
import bcrypt


class UserDAO(BaseDAO):
    model = UserOrm

    @classmethod
    def _hash_password(cls, password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

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
    def is_valid_password(cls, hashed_password: str, password: str):
        return bcrypt.checkpw(hashed_password.encode(), password.encode())
