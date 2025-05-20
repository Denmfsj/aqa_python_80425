import logging

# Створення логера
user_ms_logger = logging.getLogger('user_ms_logger')

# Налаштування рівня логування
user_ms_logger.setLevel(logging.ERROR)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('user_ms_logger.log')

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.ERROR)

# Створення форматера для обробника
formatter = logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Додавання обробника до логера
user_ms_logger.addHandler(file_handler)
