from datetime import date, datetime
from pydantic import BaseModel

from app.pdf_reports.models import ReportStatusEnum



class CreatePDFSchema(BaseModel):
    date_from: date
    date_to: date


class PDFReport(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    date_from: date
    date_to: date
    status: ReportStatusEnum
    error_message: str | None


class PDFReportDB(PDFReport):
    file_path: str | None
    user_id: str | None

