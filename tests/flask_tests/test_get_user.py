import pytest


def test_get_users(students_ctrl):
    res = students_ctrl.get_students()

    assert res.status_code == 200, 'Status code must be 200'  # первірка, що сервер повернув статус код 200

    user_ids = [k['id'] for k in res.json()]
    uniq_user_ids = set(user_ids)

    assert len(user_ids) == len(uniq_user_ids), "User ids are not unique"


@pytest.mark.parametrize('user_id', range(1,11)) # we always have first 10 users
def test_get_user(students_ctrl, user_id):
    res = students_ctrl.get_student(student_id=user_id)

    assert res.status_code == 200, 'Status code must be 200'  # первірка, що сервер повернув статус код 200
    assert res.json()['id'] == user_id, 'User id is not equal user id in request'