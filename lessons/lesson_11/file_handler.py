import logging

# Створення нового логера
request_logger = logging.getLogger("request_logger")  # __main__ або ім'я файла

# Налаштування рівня логування
request_logger.setLevel(logging.DEBUG)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('request_logs.txt')

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.INFO)

# Створення форматера для обробника
formatter = logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Додавання обробника до логера
request_logger.addHandler(file_handler)

# Логування подій
request_logger.debug('Це повідомлення рівня DEBUG')
request_logger.info('Це повідомлення рівня INFO')
request_logger.warning('Це повідомлення рівня WARNING')
request_logger.error('Це повідомлення рівня ERROR')
request_logger.critical('Це повідомлення рівня CRITICAL')