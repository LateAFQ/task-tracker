from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column (primary_key=True)
    login: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)