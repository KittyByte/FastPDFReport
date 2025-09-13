import time

from app.celery import celery_app
from app.pdf_reports.dao import ReportDAO
from app.pdf_reports.schemas import CreatePDFSchema
from app.tasks.service import send_msg_to_tg_bot



@celery_app.task(bind=True)
def create_and_send_report(self, user_id: int, data: dict):
    # task = ReportDAO.create(
        
    # )
    print('='*100)
    print(f'{user_id=}\n{data=}\n{self=}')
    print('='*100)
    
    
    send_msg_to_tg_bot("TEST", data['chat_id'])



@celery_app.task
def debug_task(time_to_sleep):
    time.sleep(time_to_sleep)
    return True

