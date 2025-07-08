from faker import Faker
import random

from sqlalchemy import create_engine, select, and_, or_, update, delete, func
from sqlalchemy.orm import sessionmaker
from core.db.tables.orm_empl_table import Employee
from core.db.tables.orm_department_table import Department
from core.db.tables.orm_base_table import Base

local_faker = Faker()

psql_conn_str = "postgresql://test_user:test_password@localhost:5432/test_db"

engine = create_engine(psql_conn_str)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


# it_dep = Department(name='IT')
# hr_dep = Department(name='HR')
# sofa_emp = Employee(name='Sofa', department=hr_dep)
# igor_emp = Employee(name='Igor', department=hr_dep)
#
# session.add_all([igor_emp])

some_user = session.query(Employee).first()

print(some_user.id)
print(some_user.name)
print(some_user.department_id)
print(some_user.department.name)


# визначити департамент юзера з id = 3


# q = session.execute(select(Employee).where(Department.name == 'IT'))
q = session.query(Employee).all()

for k in q:
    if k.department.name == 'HR':
        print(k)
# session.commit()




