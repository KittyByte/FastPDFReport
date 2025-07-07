from src.schemas.pdf import CreatePDFSchema
from src.services import send_msg_to_tg_bot




def create_pdf_report_task(data: CreatePDFSchema):
    return send_msg_to_tg_bot('TEST', data.chat_id)



