# def greetings(user_name: str) -> None:
#     """
#     this fn is printing some text
#     :param user_name: user name is a string
#     :return: None
#     """
#     print(f'Hello user {user_name}')

def multipl(number_1: int|float, number_2: int|float) -> str:
    return number_1 * number_2



# def greetings(user_name: str, user_second_name: str, user_nickname: str = '', age: int = 20) -> None:
#
#     if user_nickname:
#         user_nickname = f'a.k.a. {user_nickname}'
#
#     print(f'Hello user {user_name} {user_nickname} {user_second_name}, you are {age}')
#
#
# greetings('Alex', 'Sancho', 'Meller', 40)
# greetings('Vlad', 'Chef')
#
#
# greetings(user_nickname='Sash', user_name='Alex II', age=15, user_second_name='AA')
#
# greetings('Alex II', 'AA',  age=15, user_nickname='Sash')


# def sum_function(first_number, list_of_numbers = []):
# def sum_function(first_number, list_of_numbers = None):
#     if first_number == 0:
#         if list_of_numbers is None:
#             list_of_numbers = [5]
#     # sum(list_of_numbers) = сума всіх чисел всередені
#     print(first_number + sum(list_of_numbers))
#
# sum_function(0)
# sum_function(0)