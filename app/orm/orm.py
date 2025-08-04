from app.database import session_factory
from sqlalchemy import delete, select, insert


class BaseORM:
    model = None  # заменить потом на None

    @classmethod
    def find_one_or_none(cls, **filter_by):
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    def find_all(cls, **filter_by):
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = session.execute(query)
            return res.mappings().all()

    @classmethod
    def add(cls, **value):
        with session_factory() as session:
            new_instance = cls.model(**value)
            session.add(new_instance)
            session.commit()
            return new_instance

    @classmethod
    def add_many(cls, values: list[dict]):
        with session_factory() as session:
            query = insert(cls.model).values()
            session.execute(query)
            session.commit()

    @classmethod
    def delete(cls, **filter_by):
        with session_factory() as session:
            query = delete(cls.model).filter_by(**filter_by)
            session.execute(query)
            session.commit()


