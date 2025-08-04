from app.orm.dao import BaseDAO
from app.users.models import UserOrm


class UserDAO(BaseDAO):
    model = UserOrm

