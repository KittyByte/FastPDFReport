from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, class_mapper
from app.settings import sql_settings
from sqlalchemy import text, create_engine
from typing import Annotated
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB



engine = create_engine(url=sql_settings.DATABASE_URL, echo=True, hide_parameters=True)
session_factory = sessionmaker(engine)


class BaseOrm(DeclarativeBase):
    # https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#customizing-the-type-map
    type_annotation_map = {
        dict: JSONB
    }

    def to_dict(self):
        columns = class_mapper(self.__class__).columns
        return {column.key: getattr(self, column.key) for column in columns}


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]  # func.now() он указывает время не по UTC0, а серверное
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]
# updated_at - делать обновление лучше всего на уровне БД, в Пострес есть триггеры на автообновление записей


