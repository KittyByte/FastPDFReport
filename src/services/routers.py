from typing import Literal
from fastapi import APIRouter
from src.services.utils import drop_and_create_database, create_tables, some_sql
from typing import Any


router = APIRouter(
    prefix='/services', tags=['Service']
)


@router.get('/setup-database', description='Удаление текущей и создание новой БД. Проверить что в src.orm.services есть импорты ВСЕХ таблиц')
def setup_database() -> Literal['OK']:
    drop_and_create_database()
    return 'OK'


@router.get('/setup-tables', description='Проверить что в src.orm.services есть импорты ВСЕХ таблиц перед их созданием!')
def create_tables_api() -> Literal['OK']:
    create_tables()
    return 'OK'


@router.get('/exec-sql')
def exec_sql() -> Any:
    return some_sql()

