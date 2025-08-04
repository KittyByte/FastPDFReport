from fastapi import BackgroundTasks, APIRouter
from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.tasks import create_and_send_report


router = APIRouter(
    prefix='/report', tags=['PDF']
)


@router.post('/create')
def create_pdf_report(data: CreatePDFSchema, background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(create_and_send_report, data)
    return {"message": "Notification sent in the background"}

