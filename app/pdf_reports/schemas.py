from datetime import date, datetime
from pydantic import BaseModel

from app.pdf_reports.models import ReportStatusEnum


class BaseDBModel(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime


class CreatePDFSchema(BaseModel):
    date_from: date
    date_to: date


class PDFReportSchema(BaseDBModel):
    date_from: date
    date_to: date
    status: ReportStatusEnum
    error_message: str | None


class PDFReportDBSchema(PDFReportSchema):
    file_path: str | None
    user_id: str | None


class SalesReportSchema(BaseDBModel):
    period_from: date
    period_to: date
    total_orders: int
    total_revenue: float
    avg_order_value: float
    top_product_name: str
    top_product_sales: float
    cancelled_orders: int
    successful_orders: int
    returned_orders: int
    payment_method_stats: dict
    category_breakdown: dict
    sales_by_day: dict
    comment: str


class SalesReportDBSchema(SalesReportSchema):
    user_id: int


