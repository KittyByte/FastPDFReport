from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated
from datetime import datetime



class BaseOrm(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]  # func.now() он указывает время не по UTC0, а серверное
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]


