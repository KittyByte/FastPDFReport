from datetime import date
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, class_mapper, mapped_column

from app.database import BaseOrm


class SalesReportOrm(BaseOrm):
    __tablename__ = 'sales_report'

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

    def __repr__(self):
        # Форматированный вывод в запросах session при отладке
        cls_name = self.__class__.__name__
        columns = class_mapper(self.__class__).columns
        values = {
            column.key: getattr(self, column.key, None) for column in columns
        }
        values_str = ", ".join(f"{k}={v!r}" for k, v in values.items())
        return f"<Object: {cls_name} | Attributes: {values_str}>"



class ReportStatusEnum(Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    failed = 'failed'



class ReportOrm(BaseOrm):
    """ Хранит в себе информацию о созданном по запросу отчете """
    __tablename__ = 'report'

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    date_from: Mapped[date]
    date_to: Mapped[date]
    status: Mapped[ReportStatusEnum] = mapped_column(default=ReportStatusEnum.pending)
    file_path: Mapped[str | None]
    error_message: Mapped[str | None]

