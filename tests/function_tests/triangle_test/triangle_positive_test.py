import pytest
from utils.test_functions import triangle_area



@pytest.mark.positive  #  марки
def test_triangle_223():

    expected = 1.984313483298443
    actual = triangle_area(2,2,3)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'


@pytest.mark.users_microservice
@pytest.mark.positive
def test_triangle_888():

    expected = 27.712812921102035
    actual = triangle_area(8,8,8)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'

@pytest.mark.negative
@pytest.mark.payment_microservice
@pytest.mark.users_microservice
def test_triangle_000_negative():

    expected = 0
    actual = triangle_area(0, 0, 0)
    assert actual == expected, f'triangle area: expected: {expected} but actual is {actual}'

