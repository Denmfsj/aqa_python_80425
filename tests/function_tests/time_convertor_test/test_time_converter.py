from utils.test_functions import convert_to_24_hour
import pytest
import os



# @pytest.mark.smoke
# @pytest.mark.skipif(os.getenv('enviroment') == 'dev', reason='Dev has not actual data')  # якщо це дев, то порпустити тест
# @pytest.mark.positive
# @pytest.mark.time_converter
# def test_time_converter_smoke():
#     actual = convert_to_24_hour("3:00 AM")
#     expected = '03:00'
#
#     assert actual == expected


@pytest.mark.positive
@pytest.mark.time_converter
@pytest.mark.parametrize('expected_result, input_param', [
    ('03:00', "3:00 AM"),  # 1 test
    ('23:00', "11:00 PM")  # 2 test
])
def test_time_converter(expected_result, input_param):
    actual = convert_to_24_hour(input_param)

    assert actual == expected_result
