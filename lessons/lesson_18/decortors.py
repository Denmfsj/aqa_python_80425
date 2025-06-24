def greetings(fn_1, *args, **kwargs):  # fn_1 - функція, ярлик на фунцію ?
    print('Greetings...')
    fn_1(*args, **kwargs)


def say_hello(name):
    print(f'Hello {name}')


def print_info(name, age=55):
    print(f'name is {name}, age={age}')

# greetings(say_hello, 'Ivan')



def greetings_decorator(fn):

    def wrapper(*args, **kwargs):
        print('before function execution')
        res = fn(*args, **kwargs)
        print('after function execution')
        return res

    return wrapper


@greetings_decorator
def say_hello(name):
    print(f'Hello {name}')

# say_hello('Den')

@greetings_decorator
def sq_of_number(num):
    return num**2


my_sq = sq_of_number(12)
print(my_sq)

# print('--------------')
# greetings(print_info, 'Petro', age=70)

