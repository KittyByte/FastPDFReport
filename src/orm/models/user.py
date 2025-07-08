from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.orm.models.base import Base, intpk



class UserOrm(Base):
    __tablename__ = "user"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


