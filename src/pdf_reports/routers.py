from fastapi import BackgroundTasks, APIRouter
from src.pdf_reports.schemas import CreatePDFSchema
from src.tasks.tasks import send_msg_to_tg_bot


router = APIRouter(
    prefix='/report', tags=['PDF']
)


@router.post('/create')
def create_pdf_report(data: CreatePDFSchema, background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(send_msg_to_tg_bot, "TEST", data.chat_id)
    return {"message": "Notification sent in the background"}

