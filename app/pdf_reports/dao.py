from app.orm.dao import BaseDAO
from app.pdf_reports.models import ReportOrm


class ReportDAO(BaseDAO):
    model = ReportOrm

