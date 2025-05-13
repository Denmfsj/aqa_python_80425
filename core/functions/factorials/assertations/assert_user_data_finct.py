def assert_user_data(act, exp):


    errors = []
    field_for_checking = ['name', 'companies']
    #  soft assert

    # assert with block
    assert act['user_id'] == exp['user_id'], 'user_id is incorrect!'

    for key in field_for_checking:
        if act[key] != exp[key]:
            errors.append(f'{key}: expected is {act[key]}, actual is {exp[key]}')

    error_srt = "\n".join(errors)
    assert not errors, f'Next error we got:\n{error_srt}'