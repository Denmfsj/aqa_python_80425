# https://gorest.co.in/public/v2/users?id=7966026  Jagadish
import pytest
import requests
import time



@pytest.mark.parametrize('user_id', [7966031, 7966026, 7966021])
def test_get_users_by_id(user_id):
    response = requests.get(url='https://gorest.co.in/public/v2/users', params={'id': user_id})

    assert response.status_code == 200, f'Status code is not 200, but {response.status_code}'

    resp_data = response.json()

    assert len(resp_data) == 1, f'Response should has 1 users, but has {len(resp_data)}'

    assert resp_data[0]['id'] == user_id



@pytest.mark.parametrize('user_name', ['Den', 'Jagadish', 'asdasdasdasd'])
def test_get_users__by_name(user_name):
    response = requests.get(url='https://gorest.co.in/public/v2/users', params={'name': user_name})

    assert response.status_code == 200, f'Status code is not 200, but {response.status_code}'

    resp_data = response.json()

    for user in resp_data:
        assert user_name in user['name'], (f'{user_name} should be in name of user_id={user["id"]}, '
                                           f'name is {user["name"]}')

