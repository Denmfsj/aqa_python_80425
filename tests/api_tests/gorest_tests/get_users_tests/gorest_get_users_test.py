# https://gorest.co.in/public/v2/users?id=7966026  Jagadish
import pytest
import random
import allure

from core.api_services.gorest.gorest_endpoints import GorestEndpoint

gorest = GorestEndpoint()

@allure.story('Gorest feature')
def gorest_3_users():
    response = gorest.get_users().json()
    user_list = []

    # беремо 3 унікальних юзера
    while len(user_list) < 3:
        user = random.choice(response)
        if user in user_list:
            continue
        user_list.append(user)
    return user_list


@pytest.mark.parametrize('user_id', [user['id'] for user in gorest_3_users()])
def test_get_users_by_id(user_id):
    response = gorest.get_users(params={'id': user_id})

    response_time = response.elapsed.total_seconds()
    print(f'response_time is {response.elapsed.total_seconds()}')

    if response.elapsed.total_seconds() > 1:  # умови, що відповідь сервера повинна бути менше 1 секунди
        raise AssertionError(f'Response time is too long. Expected less than 1 sec but actual is {response_time}')


    resp_data = response.json()
    assert len(resp_data) == 1, f'Response should has 1 users, but has {len(resp_data)}'
    assert resp_data[0]['id'] == user_id



@pytest.mark.parametrize('user_name', [user['name'] for user in gorest_3_users()])
def test_get_users_by_name(user_name, session_user):
    print(session_user)
    response = gorest.get_users(params={'name': user_name})

    resp_data = response.json()  # json.loads(response.text)

    for user in resp_data:
        assert user_name in user['name'], (f'{user_name} should be in name of user_id={user["id"]}, '
                                           f'name is {user["name"]}')


@pytest.mark.skip(reason='JIRA-132, no immediately response')
def test_get_user_created_this_session(gorest_ctrl, session_user):
    """Get user that was created few minutes ago"""

    response = gorest_ctrl.get_user(user_id=session_user['id'])

    assert response.json()['id'] == session_user['id'], \
        f'Server return wrong user, expected {session_user["id"]} but actual is {response.json()["id"]}'
