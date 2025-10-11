from app.orm.dao import BaseDAO
from app.pdf_reports.models import ReportOrm, SalesReportOrm


class ReportDAO(BaseDAO):
    model = ReportOrm


class SalesReportDAO(BaseDAO):
    model = SalesReportOrm

