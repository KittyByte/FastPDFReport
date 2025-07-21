from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from app.settings import sql_settings
from sqlalchemy import text, create_engine
from typing import Annotated
from datetime import datetime


engine = create_engine(url=sql_settings.DATABASE_URL, echo=True)
session_factory = sessionmaker(engine)


class BaseOrm(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]  # func.now() он указывает время не по UTC0, а серверное
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]
# updated_at - делать обновление лучше всего на уровне БД, в Пострес есть триггеры на автообновление записей


