from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from core.db.tables.orm_base_table import Base
from sqlalchemy.orm import sessionmaker, relationship


# Визначення моделей даних (таблиць) за допомогою класів
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee",
                             back_populates="department")

