import time
import random


def calculate_data(user_ids: list):
    user_online = []


    for user in user_ids:
        # long math calculation
        time.sleep(1)
        if random.choice([1,2]) == 1:
            user_online.append(user)
        yield user
    print(f'Online were: {user_online}')
    yield user_online



user_ids = set(random.choices(range(1, 101), k=10))  #  10 випадкових чисел від 1 до 100
for k in calculate_data(user_ids):
    print(f'Checking...{k}')

# sq_numb = (k**2 for k in range(0, 21))  # generator expression, k**2 повертаеться за допомогою yield
#
# for k in sq_numb:
#     print(k)