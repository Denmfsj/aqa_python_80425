from utils.test_functions import convert_to_24_hour
import pytest
import os



@pytest.mark.negative
@pytest.mark.time_converter
@pytest.mark.xfail(reason='some reason') # якщо тести провалено - ігнорує
# @pytest.mark.skip(reason='Wait for fix in jira-123')  # не запускати тест
def test_time_converter_not_existed_time():

    with pytest.raises(ValueError):
        convert_to_24_hour("13:00 PM")
