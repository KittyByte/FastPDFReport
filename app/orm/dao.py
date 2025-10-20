from sqlalchemy import delete, insert, select, update

from app.database import session_factory


class BaseDAO:
    model = None

    @classmethod
    def find_one_by(cls, **filter_by) -> dict:
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            # __table__.columns нужен чтобы mappings выводил все поля, а не экземпляр класса
            res = session.execute(query)
            return res.mappings().one_or_none()
        # mappings делает сопоставление поля - значение, без него возвращается просто кортеж значений

    @classmethod
    def find_all_by(cls, **filter_by) -> list[dict]:
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = session.execute(query)
            return res.mappings().all()

    @classmethod
    def create(cls, **data) -> int:
        with session_factory() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = session.execute(query)
            session.commit()
            return result.mappings().first()['id']

    @classmethod
    def create_bulk(cls, values: list[dict]) -> list[int]:
        with session_factory() as session:
            query = insert(cls.model).values(values).returning(cls.model.id)
            result = session.execute(query)
            session.commit()
            return [_id['id'] for _id in result.mappings().all()]

    @classmethod
    def delete(cls, **filter_by) -> None:
        with session_factory() as session:
            query = delete(cls.model).filter_by(**filter_by)
            session.execute(query)
            session.commit()

    @classmethod
    def find_one_where(cls, where_clause) -> dict:
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter(where_clause)
            res = session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    def find_all_where(cls, *filters) -> list[dict]:
        """Поиск всех записей по сложным условиям"""
        with session_factory() as session:
            query = select(cls.model.__table__.columns).filter(*filters)
            res = session.execute(query)
            return res.mappings().all()

    @classmethod
    def update(cls, obj_id: int, **update_data) -> None:
        with session_factory() as session:
            query = (
                update(cls.model).filter_by(id=obj_id).values(update_data)
            )
            session.execute(query)
            session.commit()

