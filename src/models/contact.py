from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String, Integer, Date


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)  
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    additional_data: Mapped[str | None] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r}, fullname={self.last_name!r}, email={self.email!r}, phone_number={self.phone_number!r}, birthday={self.birthday!r}, additional_data={self.additional_data!r})"
    

# class ContactUpdate(Base):
#     first_name: Mapped[str | None] = mapped_column(nullable=True)
#     last_name: Mapped[str | None] = mapped_column(nullable=True)
#     email: Mapped[str | None] = mapped_column(nullable=True, unique=True)
#     phone_number: Mapped[str | None] = mapped_column(nullable=True)
#     birthday: Mapped[date | None] = mapped_column(Date, nullable=True)
#     additional_data: Mapped[str | None] = mapped_column(nullable=True)

#     def __repr__(self) -> str:
#         return f"User(name={self.first_name!r}, fullname={self.last_name!r}, email={self.email!r}, phone_number={self.phone_number!r}, birthday={self.birthday!r}, additional_data={self.additional_data!r})"