from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import BaseOrm, intpk, created_at, updated_at



class UserOrm(BaseOrm):
    __tablename__ = "user"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


