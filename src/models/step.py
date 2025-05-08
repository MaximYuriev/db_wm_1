from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Step(Base):
    __tablename__ = "step"
    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str]
