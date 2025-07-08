from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from src.orm.models.base_model import Base
from sqlalchemy import func
from enum import Enum


class ReportStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    failed = 'failed'



class ReportOrm(Base):
    __tablename__ = 'report'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    date_from: Mapped[datetime] = mapped_column()
    date_to: Mapped[datetime] = mapped_column()
    status: Mapped[ReportStatus] = mapped_column(default=ReportStatus.pending)
    file_path: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    error_message: Mapped[Optional[str]] = mapped_column(nullable=True)

