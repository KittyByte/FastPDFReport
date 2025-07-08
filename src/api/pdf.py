from typing import Any
from fastapi import BackgroundTasks, APIRouter
from src.schemas.pdf import CreatePDFSchema
from src.tasks import create_pdf_report_task
from src.database import *


router = APIRouter(tags=['PDF'])

@router.post('/create-pdf-report')
async def create_pdf_report(data: CreatePDFSchema, background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(create_pdf_report_task, data)
    return {"message": "Notification sent in the background"}


@router.get('/exec-sql')
async def exec_sql() -> Any:
    return get_version()
