
lst = [3, '4', 5, 6]

def calculate(number):

    try:
        is_ok = False
        res =  number / (5 - number)
    except TypeError as tp_error:
        print(f'TypeError, {tp_error}')
    except ValueError:
        print('ValueError')
    except Exception:
        print('Exception')

    else:
        print('Everything was ok')
        is_ok = True
        return res

    finally:
        if not is_ok:
            print('finally block')

for k in lst:
    print(calculate(k))
    print('-'*80)