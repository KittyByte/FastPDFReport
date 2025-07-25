from enum import Enum
from datetime import date
from app.database import BaseOrm, intpk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey



class SalesReportOrm(BaseOrm):
    __tablename__ = 'sales_report'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    period_from: Mapped[date]  # Начало периода
    period_to: Mapped[date]  # Конец периода
    total_orders: Mapped[int]  # Общее число заказов
    total_revenue: Mapped[float]  # Общая сумма выручки
    avg_order_value: Mapped[float]  # Средний чек
    top_product_name: Mapped[str]  # Самый продаваемый товар
    top_product_sales: Mapped[float]  # Сумма продаж топ-товара
    cancelled_orders: Mapped[int]  # Отменённые заказы
    successful_orders: Mapped[int]  # Успешно завершённые заказы
    returned_orders: Mapped[int]  # Возвраты
    payment_method_stats: Mapped[dict]  # Распределение по способам оплаты
    category_breakdown: Mapped[dict]  # Распределение продаж по категориям
    sales_by_day: Mapped[dict]  # Динамика по дням ({"2025-07-01": 10000, ...})
    comment: Mapped[str]  # Примечания
    created_at: Mapped[created_at]



class ReportStatus(Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    failed = 'failed'



class ReportOrm(BaseOrm):
    __tablename__ = 'report'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    date_from: Mapped[date]
    date_to: Mapped[date]
    status: Mapped[ReportStatus] = mapped_column(default=ReportStatus.pending)
    file_path: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    error_message: Mapped[str | None]

