from core.base_request_implementation import send_request
from core.utils.loggers.user_ms_logger import user_ms_logger



def get_user_info():

    # send_request()  # функція ззвоні
    # sebding request
    # if request return error:
    response = send_request(method='get', url='http://example.com', body={'a': 23})

    if response.status_code != 200:
        user_ms_logger.error('Request from ... return an error: ....')