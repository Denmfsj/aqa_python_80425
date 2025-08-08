import allure

from tests.api_tests.gorest_tests.conftest import GorestBase


@allure.feature('Negative auth')
class TestGorestNegativeAuth(GorestBase):
    def test_create_user_negative_auth_no_header(self, gorest_ctrl):


        gorest_ctrl.create_user(user_data={'name': 'asd', 'email': 'asdasd'},
                           header={},
                           expected_status_code=401)


    def test_create_user_negative_auth_wrong_auth_header(self, gorest_ctrl):

        gorest_ctrl.create_user(user_data={'name': 'asd', 'email': 'asdasd'},
                           header={'Authorization': 'asdasd'},
                           expected_status_code=401)



