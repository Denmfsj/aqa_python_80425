import pytest
import os

from constants import BASE_DIR
from utils.test_functions import triangle_area


# фікстура значить, що це можна використовувати як аргумент функції
@pytest.fixture(scope='module')  # scope = module - працює один раз перед/після всіма тестами в файлі
def prepared_users():  # ім'я каже що поверне ця функція
    user_ids = [1,2,3]
    print('\nCreating test users...\n')
    yield user_ids
    print('\nDeleting test user\n')


@pytest.fixture(scope='session', autouse=True)  # session - для запуску перед/після ВСІХ тестів в запуску
def cleanup():
    """
    Вичистка логів
    """
    yield
    for name in ['log.log', 'error.log']:
        print(f'Searching {BASE_DIR / name}')

        if (BASE_DIR/name).exists():
            print(f'deleting {BASE_DIR/name}')

@pytest.mark.positive  #  марки
def test_triangle_223(prepared_users):

    print(f'\nUsers was created {prepared_users}\n')
    expected = 1.984313483298443
    actual = triangle_area(2,2,3)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'


@pytest.mark.users_microservice
@pytest.mark.positive
def test_triangle_888(prepared_users):

    print(f'\nUsers was created {prepared_users}\n')
    expected = 27.712812921102035
    actual = triangle_area(8,8,8)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'

@pytest.mark.negative
@pytest.mark.payment_microservice
@pytest.mark.users_microservice
def test_triangle_000_negative():

    if not os.path.exists('res_folder'):
        os.mkdir('res_folder')

    with open('res_folder/test_data.txt', 'w') as f:
        f.write('text from test')

    expected = 0
    actual = triangle_area(0, 0, 0)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'

