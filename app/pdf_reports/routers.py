from fastapi import APIRouter, BackgroundTasks, Depends

from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.tasks import create_and_send_report
from app.security import oauth2_scheme


router = APIRouter(
    tags=['PDF'],
    prefix='/report', 
    dependencies=[Depends(oauth2_scheme)]
)


@router.post('/create')
def create_pdf_report(data: CreatePDFSchema, background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(create_and_send_report, data)
    return {"message": "Notification sent in the background"}

