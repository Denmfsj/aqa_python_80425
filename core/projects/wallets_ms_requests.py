from core.base_request_implementation import send_request
from core.utils.loggers.wallet_ms_logger import wallet_ms_logger


def get_wallet_info():

    # send_request()
    # if request return error:
    response = send_request(method='post', url='http://example.com', body={'a': 23})

    if response.status_code != 201:
        wallet_ms_logger.error('Request from ... return an error: ....')

