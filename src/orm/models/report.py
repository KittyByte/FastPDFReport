from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from src.orm.models.base import Base, intpk
from sqlalchemy import ForeignKey, text
from enum import Enum


class ReportStatus(Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    failed = 'failed'



class ReportOrm(Base):
    __tablename__ = 'report'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]
    status: Mapped[ReportStatus] = mapped_column(default=ReportStatus.pending)
    file_path: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))  # func.now() он указывает время не по UTC0, а серверное
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)
    error_message: Mapped[str | None]

