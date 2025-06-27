# https://gorest.co.in/public/v2/users?id=7966026  Jagadish

import time

from core.api_services.gorest.gorest_endpoints import GorestEndpoint

gorest = GorestEndpoint()

def test_get_users_smoke():
    response = gorest.get_users()

    assert len(response.json()) > 0, 'Response should not be empty'


def test_get_user_v2_smoke():
    response = gorest.get_user(5566)

    assert len(response.json()) == 0, 'Response should be empty'


def test_get_user_v1_smoke():
    response = gorest.get_user(5566, gorest.version1)

    assert len(response.json()) > 0, 'Response should not be empty'


def test_create_user_with_existed_email_smoke():

    gorest.create_user(
        user_data={"name": "Tenali Ramakrishna", "gender": "male",
              "email": f"tenali.ramakrishna@gmail.com", "status": "active"},
    expected_status_code=422)


def test_create_user_smoke():

    response = gorest.create_user(
        user_data={"name": "Tenali Ramakrishna", "gender": "male",
              "email": f"tenali.ramakrishna@gmail.com", "status": "active"})

    assert len(response.json()) > 0, 'Response should not be empty'

