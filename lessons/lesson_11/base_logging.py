import logging

# Налаштування конфігурації логування
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

# Додавання обробника для виводу в консоль
console_handler = logging.StreamHandler() # повертає об'єкт handler який вміє записувати в консоль
console_handler.setLevel(logging.INFO)  # встановлюємо якого рівня повідомлення будуть писатись за допомогою console_handler

logging.getLogger('').addHandler(console_handler)  # ми вмикаємо console_handler як частину загального логера

# Логування подій різного рівня
logging.debug('Це повідомлення рівня DEBUG')
logging.info('Це повідомлення рівня INFO')
logging.warning('Це повідомлення рівня WARNING')
logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')