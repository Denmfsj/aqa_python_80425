# https://gorest.co.in/public/v2/users?id=7966026  Jagadish

import requests
import time


def test_get_users_smoke():
    response = requests.get(url='https://gorest.co.in/public/v2/users')

    assert response.status_code == 200, f'Status code is not 200, but {response.status_code}'

    assert len(response.json()) > 0, 'Response should not be empty'


def test_create_user_smoke():
    response = requests.post(
        url='https://gorest.co.in/public/v2/users',
        json={"name": "Tenali Ramakrishna", "gender": "male",
              "email": f"tenali.ramakrishna@{time.time()}.com", "status": "active"},
        headers={
            "Authorization": "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e"})

    assert  response.status_code == 201,  f'Status code is not 201, but {response.status_code}'
    assert len(response.json()) > 0, 'Response should not be empty'
