import pytest


class TestDeletingUsersFirstTime:

    def test_delete_user(self, new_user, gorest_ctrl, session_user):
        print(session_user)
        user_id = new_user.json()['id']
        gorest_ctrl.delete_user(user_id)


class TestDeletingUsersSecondTime:

    @pytest.mark.parametrize('number', range(2))
    def test_delete_user2(self, number, new_user, gorest_ctrl, session_user):
        print(session_user)
        user_id = new_user.json()['id']
        gorest_ctrl.delete_user(user_id)