

def test_create_user_negative_auth_no_header(gorest_ctrl):


    gorest_ctrl.create_user(user_data={'name': 'asd', 'email': 'asdasd'},
                       header={},
                       expected_status_code=401)


def test_create_user_negative_auth_wrong_auth_header(gorest_ctrl):

    gorest_ctrl.create_user(user_data={'name': 'asd', 'email': 'asdasd'},
                       header={'Authorization': 'asdasd'},
                       expected_status_code=401)



