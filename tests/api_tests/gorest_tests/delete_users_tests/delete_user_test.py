import allure
import pytest
from allure_commons.types import LinkType

from tests.api_tests.gorest_tests.conftest import GorestBase


@allure.feature('Delete user')
class TestDeletingUsersFirstTime(GorestBase):

    @allure.link('jira-bug.com', link_type=LinkType.ISSUE)
    @allure.story('Deleting standard user')
    def test_delete_user(self, new_user, gorest_ctrl, session_user):
        print(session_user)
        user_id = new_user.json()['id']
        gorest_ctrl.delete_user(user_id)


@allure.feature('Delete user')
class TestDeletingUsersSecondTime(GorestBase):

    @allure.link('jira-test-rail-test-id.com', link_type=LinkType.TEST_CASE)
    @allure.story('Delete user second time')
    @pytest.mark.parametrize('number', range(2))
    def test_delete_user2(self, number, new_user, gorest_ctrl, session_user):
        print(session_user)
        user_id = new_user.json()['id']
        gorest_ctrl.delete_user(user_id)