import pytest


@pytest.mark.parametrize('is_active', [True, False])
@pytest.mark.parametrize('name', ['Den', 'Alex', 'Ivan'])
@pytest.mark.parametrize('age', [18,19,30,65,66])
def test_test_user_search(name, age, is_active):

    print(f'Searching of {name} or {age}, {is_active}')
