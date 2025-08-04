from app.database import session_factory
from sqlalchemy import delete, select, insert


class BaseDAO:
    model = None

    @classmethod
    def find_one_or_none(cls, **filter_by):
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            # __table__.columns нужен для корректной работы mappings
            res = session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    def find_all(cls, **filter_by):
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = session.execute(query)
            return res.mappings().all()

    @classmethod
    def create(cls, **data):
        with session_factory() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = session.execute(query)
            session.commit()
            return result.mappings().first()

    @classmethod
    def create_bulk(cls, values: list[dict]):
        with session_factory() as session:
            query = insert(cls.model).values(values).returning(cls.model.id)
            result = session.execute(query)
            session.commit()
            return result.mappings().all()

    @classmethod
    def delete(cls, **filter_by):
        with session_factory() as session:
            query = delete(cls.model).filter_by(**filter_by)
            session.execute(query)
            session.commit()


