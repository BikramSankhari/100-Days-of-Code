from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine("sqlite:///Self_Referencing_Foreign_Key.db")


class Base(DeclarativeBase):
    pass


class Employees(Base):
    __tablename__ = "employee_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    manager_id: Mapped[int] = mapped_column(ForeignKey("employee_table.id"), nullable=True)

    manager: Mapped["Employees"] = relationship()


Base.metadata.create_all(engine)
