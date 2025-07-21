""" указывать тут все импорты для корректной работы create_all И drop_all """
from app.pdf_reports.models import *
from app.users.models import *

from app.database import BaseOrm, session_factory, engine
from datetime import datetime


def some_sql():
    with session_factory() as session:
        report = PDFReportOrm(
            path_to_file='pathhhh',
            date_from=datetime.now(),
            date_to=datetime.now()
        )
        session.add(report)
        session.commit()
    return 'OK'


def create_tables():
    BaseOrm.metadata.create_all(engine)


def drop_and_create_database():
    print(BaseOrm.metadata.tables.keys())
    print('='*100)
    BaseOrm.metadata.drop_all(engine)
    create_tables()

