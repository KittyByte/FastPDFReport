import requests

from app.pdf_reports.dao import ReportDAO
from app.pdf_reports.schemas import CreatePDFSchema
from app.settings import settings


def send_msg_to_tg_bot(msg, chat_id: int) -> dict:
    return requests.post(
        f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={'chat_id': chat_id, 'text': msg}
    ).json()


def create_and_send_report(data: CreatePDFSchema):
    # task = ReportDAO.create(
        
    # )
    
    
    send_msg_to_tg_bot("TEST", data.chat_id)



