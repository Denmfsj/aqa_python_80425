

# def division(a, b):
#
#     if not (type(a) is int and type(b) is int):
#         print('You have to use numbers')
#         return
#
#     if b == 0:
#         print('You cant divide by 0')
#         return
#
#     return a / b


def division(a, b):

    try:
        result =  a / b  # блок коду в якому очікуеться помилка
        [1,2][555]  # IndexError
        return result

    # except ZeroDivisionError:
    #     print('You cant divide by 0')
    #
    # except TypeError:
    #     print('You have to use numbers')

    except (TypeError, ZeroDivisionError) as e:  # записав помилку як об'єкт в змінну e
        print(f'Smth was wrong\n{e}')

    except Exception as e:
        print('Exception was called')
        print(e)


    print('Done of calculation')

division(1,0)
print('--'*40)
division(1,'0')
print('--'*40)
division(1,1)
#
# ZeroDivisionError < ArithmeticError < Exception
# TypeError < Exception
# IndexError < Exception