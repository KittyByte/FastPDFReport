from fastapi import APIRouter
from fastapi.responses import HTMLResponse, FileResponse

from app.pdf_reports.schemas import CreatePDFSchema, PDFReport
from app.tasks.tasks import create_and_send_report
from app.users.dependencies import GetCurrentActiveUserDep
from app.pdf_reports.dao import ReportDAO



router = APIRouter(
    tags=['PDF'],
    prefix='/report'
)


@router.post('/create')
def create_pdf_report(current_user: GetCurrentActiveUserDep, data: CreatePDFSchema) -> dict:
    create_and_send_report.delay(current_user.id, data.model_dump(mode='json'))
    return {"success": True}


@router.get('/items')
def get_pdf_reports(current_user: GetCurrentActiveUserDep) -> list[PDFReport]:
    return ReportDAO.find_all(user_id=current_user.id)


@router.get('/reports')
def get_html_pdf_reports() -> HTMLResponse:
    return FileResponse('app/static/reports_menu.html')

