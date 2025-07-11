# https://gorest.co.in/public/v2/users?id=7966026  Jagadish



def test_get_users_smoke(gorest_ctrl):
    response = gorest_ctrl.get_users()

    assert len(response.json()) > 0, 'Response should not be empty'


def test_get_user_v2_version_of_endpoint_smoke(gorest_ctrl):
    response = gorest_ctrl.get_user(5566)

    assert len(response.json()) == 0, 'Response should be empty'


def test_get_user_v1_version_of_endpoint_smoke(gorest_ctrl):
    response = gorest_ctrl.get_user(5566, gorest_ctrl.version1)

    assert len(response.json()) > 0, 'Response should not be empty'


def test_create_user_with_existed_email_smoke(gorest_ctrl):

    gorest_ctrl.create_user(
        user_data={"name": "Tenali Ramakrishna", "gender": "male",
              "email": f"tenali.ramakrishna@gmail.com", "status": "active"},
    expected_status_code=422)

