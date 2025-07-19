from typing import Literal
from fastapi import APIRouter
from src.database import drop_and_create_database, create_tables
from typing import Any
from src.database import some_sql


router = APIRouter(tags=['Service'])


@router.get('/setup-database', description='Удаление текущей и создание новой БД')
async def setup_database() -> Literal['OK']:
    drop_and_create_database()
    return 'OK'


@router.get('/setup-tables', description='Проверить все импорты таблиц перед их созданием!')
async def create_tables_api() -> Literal['OK']:
    create_tables()
    return 'OK'



@router.get('/exec-sql')
async def exec_sql() -> Any:
    return some_sql()
