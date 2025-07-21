from enum import Enum
from datetime import datetime
from app.database import BaseOrm, intpk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey



class PDFReportOrm(BaseOrm):
    __tablename__ = 'pdf_report'

    id: Mapped[intpk]
    path_to_file: Mapped[str]
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]



class ReportStatus(Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    failed = 'failed'



class ReportOrm(BaseOrm):
    __tablename__ = 'report'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]
    status: Mapped[ReportStatus] = mapped_column(default=ReportStatus.pending)
    file_path: Mapped[str] = mapped_column()
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    error_message: Mapped[str | None]

