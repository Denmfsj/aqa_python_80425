import pytest
import requests



def test_create_user_negative_auth_no_header():


    response = requests.post(url='https://gorest.co.in/public/v2/users',
                             body={'name': 'asd', 'email': 'asdasd'})

    assert response.status_code == 401, (f'Response should have status code 401, '
                                         f'but it has {response.status_code}')


def test_create_user_negative_auth_wrong_auth_header():


    response = requests.post(url='https://gorest.co.in/public/v2/users',
                             body={'name': 'asd', 'email': 'asdasd'},
                             headers={'Authoriztion': 'asdasd'})

    assert response.status_code == 403, (f'Response should have status code 403, '
                                         f'but it has {response.status_code}')


