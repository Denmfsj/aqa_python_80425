def skip_errors(fn):

    def wrapper(*args, **kwargs):
        try:
           return fn(*args, **kwargs)
        except Exception as e:
            print(f'Cant run because of {e}')

    return wrapper


@skip_errors
def division(num1, num2):
    return num1/num2

division(1,0)
