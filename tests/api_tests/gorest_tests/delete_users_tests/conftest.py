import pytest
import time


@pytest.fixture  # фікстура буде створювати юзера для кожного теста який її використовує
def new_user(gorest_ctrl, faker):
    email = f'{time.time()}-{faker.email()}'
    return gorest_ctrl.create_user(user_data={'name': faker.name(),
                                              'email': email,
                                              "gender": "male",
                                              "status": "active"})