from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from core.db.tables.orm_base_table import Base
from sqlalchemy.orm import sessionmaker, relationship


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department",
                              back_populates="employees")


    def __str__(self):
        return f'{self.id}:{self.name}'


class Realtion(Base):
    __tablename__ = 'relations'

    student_id = Column(Integer, primary_key=True)
    course_id = Column(String)


    # Встановлення відношення "багато до одного" з таблицею Department
    stud = relationship("Student",
                              back_populates="employees")
    # Встановлення відношення "багато до одного" з таблицею Department
    course = relationship("Course",
                              back_populates="employees")


    def __str__(self):
        return f'{self.id}:{self.name}'