import time

def skip_errors(fn):

    def wrapper(*args, **kwargs):
        try:
           return fn(*args, **kwargs)
        except Exception as e:
            print(f'Cant run because of {e}')

    return wrapper

def retry(max_retries, time_between_tries=3, type_of_error=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except type_of_error as e:
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
                time.sleep(time_between_tries)  # чекати time_between_tries секунд
            raise type_of_error("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator


@retry(2, time_between_tries=1)
def connect_to_server():

    raise ConnectionError("Не вдалося підключитися до сервера")

# Виклик функції
connect_to_server()