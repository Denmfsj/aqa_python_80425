
import requests

import logging

def request_logger():  # окремий файл

    r_logger = logging.getLogger('request_method')
    r_logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('requests_logger.log')
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    r_logger.addHandler(file_handler)

    return r_logger

def send_request(method, url, **kwargs):
    logger = request_logger()
    logger.info(f'sending request {method} to {url}')

    if method == 'get':
        return requests.get(url=url, **kwargs)