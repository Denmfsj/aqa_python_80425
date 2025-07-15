# https://gorest.co.in/public/v2/users?id=7966026  Jagadish
import pytest
import random

from core.api_services.gorest.gorest_endpoints import GorestEndpoint

gorest = GorestEndpoint()



def default_3_users():
    response = gorest.get_users().json()
    user_list = []

    # беремо 3 унікальних юзера
    while len(user_list) < 3:
        user = random.choice(response)
        if user in user_list:
            continue
        user_list.append(user)
    return user_list


# default_3_users() = list[dict, dict, dict]
@pytest.fixture(params=default_3_users(), scope='session')
def gorest_3_random_users(request):
    return request.param  # -> dict


def test_get_users_by_name(gorest_3_random_users, request):

    print(f'current test is {request.node.name}')

    user_id = gorest_3_random_users['id']
    response = gorest.get_users(params={'id': user_id})

    response_time = response.elapsed.total_seconds()
    print(f'response_time is {response.elapsed.total_seconds()}')

    if response.elapsed.total_seconds() > 1:  # умови, що відповідь сервера повинна бути менше 1 секунди
        raise AssertionError(f'Response time is too long. Expected less than 1 sec but actual is {response_time}')

    resp_data = response.json()
    assert len(resp_data) == 1, f'Response should has 1 users, but has {len(resp_data)}'
    assert resp_data[0]['id'] == user_id

