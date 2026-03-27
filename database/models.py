from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

class UserMessages(Base):
    __tablename__ = "user_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, index=True, nullable=False)
    role: Mapped[str] = mapped_column(String(10))
    content: Mapped[str] = mapped_column()