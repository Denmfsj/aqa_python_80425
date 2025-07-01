import psycopg2
import pytest
from faker import Faker


f = Faker()

dbname = 'test_db'
user = 'test_user'
password = 'test_password'
host = 'localhost'
port = 5432


@pytest.fixture(scope='session')
def connection():
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")
    yield connection
    connection.close()


@pytest.fixture(scope='session')
def cursor(connection):
    cursor = connection.cursor()
    yield cursor
    cursor.close()


@pytest.fixture(scope='session')
def cursor_conn(connection, cursor):
    yield connection, cursor
    connection.commit()




def test_insert_user(cursor_conn):

    conn, cursor = cursor_conn

    expected_user_name = f.name()
    expected_user_descr = f.job()

    cursor.execute(f"""INSERT 
    INTO public."user" ("name", "description") 
    VALUES ('{expected_user_name}', '{expected_user_descr}') 
    RETURNING id;""") # повернеться id створеного юзера

    new_user_id = cursor.fetchone()[0]  # cursor.fetchone() -> tuple(id, )

    cursor.execute(f"""Select "name", "description" from "user" where "id" = {new_user_id}""")

    conn.rollback()

    actual_user_name, actual_user_descr = cursor.fetchone()  # cursor.fetchone() -> tuple(name, description)

    assert actual_user_name == expected_user_name
    assert actual_user_descr == expected_user_descr




