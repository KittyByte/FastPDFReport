from sqlalchemy import text, create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from src.settings import sql_settings



# async_engine = create_async_engine(
#     url=sql_settings.ASYNC_DATABASE_URL,
#     # echo=True
# )


# async def get_version():
#     async with engine.connect() as conn:
#         res = await conn.execute(text('SELECT VERSION()'))
#         print(f'{res.first()=}')


engine = create_engine(
    url=sql_settings.DATABASE_URL_SQLITE
)


def get_version():
    with engine.connect() as conn:
        res = conn.execute(text('SELECT 1')).first()
    print(f'{res=}')
    return str(res)
