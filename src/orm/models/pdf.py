from datetime import datetime
from sqlalchemy.orm import Mapped
from src.orm.models.base import Base, intpk, created_at, updated_at



class PDFReportOrm(Base):
    __tablename__ = 'pdf_report'

    id: Mapped[intpk]
    path_to_file: Mapped[str]
    date_from: Mapped[datetime]
    date_to: Mapped[datetime]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

