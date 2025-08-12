from utils.settings import d_settings
from utils.test_functions import convert_to_24_hour
import pytest
import logging



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
    ('23:00', "11:00 PM"),  # 2 test
    ('23:00', "12:00 PM"),  # 3 test
    ('20:00', "8:00 PM"),  # 2 test
    ('09:00', "9:00 AM"),  # 2 test
])
def test_time_converter(expected_result, input_param):
    logging.info(f'Run test test_time_converter with {expected_result} and {input_param}')
    actual = convert_to_24_hour(input_param)

    log_results(expected_result, actual)

    assert expected_result == actual


@pytest.mark.time_converter
def test_check_env_vars():
    assert d_settings.secret_phrase == 'prod_phrase'

@pytest.mark.time_converter
def test_check_pwd():
    assert d_settings.user_pwd == 'secret_sauce'


def log_results(exp, act):
    if exp != act:
        logging.error(f'{__name__}: Data is incorrect expected is {exp} but actual is {act}')
