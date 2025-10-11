import time

from app.celery import celery_app
from app.pdf_reports.dao import ReportDAO
from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.service import send_msg_to_tg_bot
from app.users.dao import UserDAO


@celery_app.task(bind=True)
def create_and_send_report(self, user_id: int, data: dict):
    data_schema = CreatePDFSchema(**data)
    user = UserDAO.find_one_or_none(id=user_id)

    task_id = ReportDAO.create(
        user_id=user.id,
        date_from=data_schema.date_from,
        date_to=data_schema.date_to
    )

    task = ReportDAO.find_one_or_none(id=task_id)

    send_msg_to_tg_bot(f"TEST {task_id=} {task=}", user.telegram_id)
    return True


@celery_app.task
def debug_task(time_to_sleep):
    time.sleep(time_to_sleep)
    return True

