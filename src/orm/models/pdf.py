from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from src.orm.models.base import Base, intpk



class PDFReportOrm(Base):
    __tablename__ = 'pdf_report'

    id: Mapped[intpk]
    create_at: Mapped[datetime] = mapped_column(default=datetime.now)
    path_to_file: Mapped[str]
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]

