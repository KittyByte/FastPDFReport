from fastapi import APIRouter

from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.tasks import create_and_send_report
from app.users.dependencies import GetCurrentActiveUserDep


router = APIRouter(
    tags=['PDF'],
    prefix='/report'
)


@router.post('/create')
def create_pdf_report(current_user: GetCurrentActiveUserDep, data: CreatePDFSchema) -> dict:
    create_and_send_report.delay(current_user.id, data.model_dump(mode='json'))
    return {"message": "Notification sent in the background"}

