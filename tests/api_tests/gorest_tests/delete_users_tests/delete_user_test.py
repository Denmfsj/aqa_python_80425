


def test_delete_user(new_user, gorest_ctrl, session_user):
    print(session_user)
    user_id = new_user.json()['id']
    gorest_ctrl.delete_user(user_id)