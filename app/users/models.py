from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import BaseOrm, created_at, intpk, updated_at


class UserOrm(BaseOrm):
    __tablename__ = "user"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]
    fullname: Mapped[str | None]
    email: Mapped[str | None]
    disabled: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __repr__(self) -> str:
        return (
            f"<Table: User(id={self.id!r}, username={self.username!r}, "
            f"fullname={self.fullname!r}), disabled={self.disabled!r})>"
        )
