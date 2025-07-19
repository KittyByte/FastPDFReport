from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from src.settings import sql_settings
from src.orm.models import Base, PDFReportOrm


# async_engine = create_async_engine(
#     url=sql_settings.ASYNC_DATABASE_URL,
#     # echo=True
# )


# async def get_version():
#     async with engine.connect() as conn:
#         res = await conn.execute(text('SELECT VERSION()'))
#         print(f'{res.first()=}')


engine = create_engine(url=sql_settings.DATABASE_URL, echo=True)
session_factory = sessionmaker(engine)


def some_sql():
    with session_factory() as session:
        res = session.add(PDFReportOrm(
            
        ))
    print(f'{res=}')
    return str(res)




def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def drop_and_create_database():
    Base.metadata.drop_all(engine)
    create_tables()

