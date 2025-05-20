import logging

# Створення логера
wallet_ms_logger = logging.getLogger('wallet_ms_logger')

# Налаштування рівня логування
wallet_ms_logger.setLevel(logging.ERROR)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('wallet_ms_logger.log')
cli_handler = logging.StreamHandler()

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.ERROR)
cli_handler.setLevel(logging.INFO)

# Створення форматера для обробника
formatter = logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
cli_handler.setFormatter(formatter)

# Додавання обробника до логера
wallet_ms_logger.addHandler(file_handler)
wallet_ms_logger.addHandler(cli_handler)
