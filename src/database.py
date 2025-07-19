from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.settings import sql_settings
from src.orm.models import BaseOrm, PDFReportOrm


engine = create_engine(url=sql_settings.DATABASE_URL, echo=True)
session_factory = sessionmaker(engine)


def some_sql():
    with session_factory() as session:
        res = session.add(PDFReportOrm(
            
        ))
    print(f'{res=}')
    return str(res)


def create_tables():
    BaseOrm.metadata.drop_all(engine)
    BaseOrm.metadata.create_all(engine)


def drop_and_create_database():
    BaseOrm.metadata.drop_all(engine)
    create_tables()

