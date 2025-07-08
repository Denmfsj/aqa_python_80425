from faker import Faker
import random
import time

from requests import session
from sqlalchemy import create_engine, select, and_, or_, update, delete, func
from sqlalchemy.orm import sessionmaker
from core.db.tables.orm_user_table import OrmUser, Base

local_faker = Faker()

psql_conn_str = "postgresql://test_user:test_password@localhost:5432/test_db"

engine = create_engine(psql_conn_str)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# аналог insert
# users = [
#     OrmUser(name='Alex', age=20),
#     OrmUser(name='Ivan', age=26),
# ]
users = [
    OrmUser(
        name=f'test-{local_faker.name()}',
        age=random.choice(range(18, 66))
    )
    for k in range(5)
]
session.add_all(users)
session.commit()

new_user = OrmUser(name='Alex', age=20)
user = session.query(OrmUser).filter_by(id=10).first()  # user = OrmUser(id=10, name='test-Alicia Elliott', age=45)

# print(user)

#  створення запиту, аналог створення sql строки
# select_query = select(OrmUser).where(OrmUser.id<20).where(OrmUser.name.startswith('test')).where(OrmUser.age - 10 > 20)

select_query = select(OrmUser).where(
    and_(
        OrmUser.id<20,    # id < 20 and (age < 30 OR age > 50)
        # and
        or_(OrmUser.age < 30 , OrmUser.age > 50)))


select_result = session.execute(select_query)  # виконання sql

# print(select_result)
getted_users = [k[0] for k in select_result]

# for k in getted_users:
#     print(k)
#     k.name = f'test - {local_faker.name()}'
#     print(k)
#     print('-------------------')
#

update_query = update(OrmUser).where(OrmUser.id < 10).values(age=100)
session.execute(update_query)

delete_query = delete(OrmUser).where(OrmUser.id > 150)
session.execute(delete_query)

session.commit()
session.close()

# select sum(age)
select_result = session.query(OrmUser).order_by(OrmUser.id.asc()).limit(20)
sum_of_age_of_first_20_users = [k for k in session.execute(select(func.sum(OrmUser.age)).where(OrmUser.id < 20))]


for k in select_result:
    print(k)
print(sum_of_age_of_first_20_users)
print(session.query(func.sum(OrmUser.age)).scalar())  # кількість строк в таблиці

# select sum(age) from user where if < 20  # поверне сумму всіх age для всіє таблиці(1 число)