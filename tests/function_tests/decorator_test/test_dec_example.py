import pytest


@pytest.mark.parametrize('age', [2,5,8,7,])
@pytest.mark.parametrize('name', ['Alex', 'Ivan', 'Georg'])
def test_dec_example(name, age):

    print(f'{name}, {age}')


