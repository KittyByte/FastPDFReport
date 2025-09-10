from typing import Any, Literal

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.utils import (
    create_tables, drop_and_create_database, some_sql
)
from app.celery import debug_task


router = APIRouter(
    prefix='/services', tags=['Service']
)


@router.get('/setup-database', description='Удаление текущей и создание новой БД. Проверить что в app.orm.services есть импорты ВСЕХ таблиц')
def setup_database() -> Literal['OK']:
    drop_and_create_database()
    return 'OK'


@router.get('/setup-tables', description='Проверить что в app.orm.services есть импорты ВСЕХ таблиц перед их созданием!')
def create_tables_api() -> Literal['OK']:
    create_tables()
    return 'OK'


@router.get('/exec-sql')
def exec_sql() -> Any:
    return some_sql()


@router.post("/tasks", status_code=201)
def run_task(time_to_sleep: int):
    task = debug_task.delay(int(time_to_sleep))
    return JSONResponse({"task_id": task.id})
