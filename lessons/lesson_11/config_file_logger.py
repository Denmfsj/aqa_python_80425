import logging.config


logging.config.fileConfig('../../../config_logger.ini')  # вказуємо на шлях до файла конфігурація


# Використання логера
my_logger = logging.getLogger('sampleLogger')



