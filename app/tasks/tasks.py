import time
from datetime import date
from app.services.generate_pdf_report import generate_report_pdf
from sqlalchemy import and_
import logging

from app.celery import celery_app
from app.pdf_reports.dao import ReportDAO, SalesReportDAO
from app.pdf_reports.models import ReportOrm, SalesReportOrm, ReportStatusEnum
from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.service import send_doc_and_msg_to_tg_bot
from app.users.dao import UserDAO


@celery_app.task(bind=True)
def create_and_send_report(self, user_id: int, data: dict):
    logging.info(f"Start create_and_send_report task for {user_id=} with {data=}")
    data_schema = CreatePDFSchema(**data)

    user = UserDAO.find_one_by(id=user_id)
    task_id = ReportDAO.create(
        user_id=user.id,
        date_from=data_schema.date_from,
        date_to=data_schema.date_to
    )

    task = ReportDAO.find_one_by(id=task_id)
    time.sleep(10)  # Имитировать долгую работу

    sales = SalesReportDAO.find_all_where(
        and_(
            SalesReportOrm.period_from >= data_schema.date_from,
            SalesReportOrm.period_to <= data_schema.date_to
        )
    )

    file_path = generate_report_pdf(sales)
    # task['file_path'] = file_path
    # task['status'] = ReportStatusEnum.done
    ReportDAO.update(task.id, file_path=str(file_path), status=ReportStatusEnum.done)

    logging.info(f"End create_and_send_report task for {user_id=} with {data=}")
    if not file_path:
        return False
    send_doc_and_msg_to_tg_bot(f"TEST {task_id=} {task=}", user.telegram_id, file_path)
    return True


@celery_app.task
def debug_task(time_to_sleep):
    time.sleep(time_to_sleep)
    return True

