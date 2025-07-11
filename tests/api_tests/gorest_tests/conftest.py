# conftest.py

import time

import pytest

from core.api_services.gorest.gorest_endpoints import GorestEndpoint


@pytest.fixture(scope='module')  # фікстура буде створювати юзера для кожного теста який її використовує
def session_user(gorest_ctrl):
    email = f'test-{time.time()}@asd.com'
    user = gorest_ctrl.create_user(user_data={'name': 'test-user',
                                              'email': email,
                                              "gender": "male",
                                              "status": "active"})

    print(f'CREATING SESSION USER, {user.json()}')

    yield user.json()

    gorest_ctrl.delete_user(user_id=user.json()['id'])


@pytest.fixture(scope='session')
def gorest_ctrl():
    return GorestEndpoint()