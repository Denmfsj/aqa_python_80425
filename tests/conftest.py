import pytest
from faker import Faker
from random import choice
from core.api_services.local_student_service.student_controller import StudentController


faker = Faker()

@pytest.fixture(scope='session')
def students_ctrl():
    return StudentController()

@pytest.fixture(scope='session', autouse=True)
def create_n_users(students_ctrl):
    for _ in range(10):
        st_data = {'name': faker.name(), 'score': choice(range(1, 101))}
        students_ctrl.create_student(st_data)


