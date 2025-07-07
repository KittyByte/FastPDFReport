from sqlalchemy import create_engine, text
from src.settings import sql_settings



engine = create_engine(
    url=sql_settings.DATABASE_URL,
    # echo=True
)


with engine.connect() as conn:
    res = conn.execute(text('SELECT VERSION()'))
    print(f'{res=}')