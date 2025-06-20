import time

# geenrator
def give_3_names():
    print('First call')
    yield 'Den'  # yield - оператор преривання

    print('Second call')
    yield 'Alex'

    print('Third call')
    yield 'Ivan'


def calculate_data(number_of_calculation):

    for k in range(number_of_calculation):
        # long math calculation
        time.sleep(1)
        yield k**2  # зупиняеться і продовжує роботу з цього місця
#
#
# for sq in calculate_data(3):
#     print(sq)
#

start_time =time.time()  #  поточний час в секундах




for k in range(2000000):
    print(k)
print(time.time()  - start_time)



# print(give_3_names())
# iter_from_gen = iter(give_3_names())
# next(iter_from_gen)
# next(iter_from_gen)
# next(iter_from_gen)
# next(iter_from_gen)