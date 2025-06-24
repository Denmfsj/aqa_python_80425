import time
import random


def set_execution_time(ex_time):
    def decorator(func):
        def wrapper(*args, **kwargs):

            start_time = time.time()  # поточний час в мілісекундах
            res = func(*args, **kwargs)
            end_time = time.time()

            time_of_execution_of_fn = end_time - start_time

            if time_of_execution_of_fn < ex_time:
                time.sleep(ex_time - time_of_execution_of_fn)

            print(f'execution_time is {time.time() - start_time}')
            return res

        return wrapper
    return decorator

@set_execution_time(10)
def sending_request():
    print('sending request')
    random.choices(range(1, 6))

@set_execution_time(3)
def sending_request_2():
    print('sending request')
    random.choices(range(1, 6))  #  чекати від 1 до 5 секунд, випадково

sending_request()
