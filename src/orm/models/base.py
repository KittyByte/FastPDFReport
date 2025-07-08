from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]


