#
#
# # result = all([True, True, True])
# # print(result)
# # print(all([True, True, False]))
# #
# #
# # # my_descr = 'My name is  Den'.split(' ')
# # # print(my_descr)
# # #
# # # # my_descr = ['My', 'name', 'is', '', 'Den']
# # # result_2 = all(my_descr)  # [bool('My'), bool('name'), bool('is'), bool(''), bool('Den')]
# # # print(result_2)
# #
# # print(any([False, False]))
# # print(any([1, 2, 5, 0]))
# # print(all([1, 2, 5, 0]))
#
# users = [
#     {'age': 30}, {'age': 40}, {'age': 25}
# ]
#
#
# #
# # is_over_30 = [k['age'] >= 30 for k in users]
# # print(users)
# # print('Anyone older than 30:', any(is_over_30))
#
#
# # enumerate()
#
# # user_counter = 0
# # for user in users:
# #     print(f'User number {user_counter + 1} has age {user["age"]}')
# #     user_counter += 1
#
# # for user_index, user in enumerate(users):
# #     print(f'User number {user_index + 1} has age {user["age"]}')
#
#
# my_list_of_numbers = list(range(10,21))  # від 10 до 20, але в випаковому порядку
#
# reversed_list = my_list_of_numbers[::-1]
#
# user = {'age': 30, 'id': 20, 'name': 'Alex'}
#
# #
# # for index, number in enumerate(reversed_list):
# #     print(f'Number {number} has index {index}')
#
# for index, user_data in enumerate(user.items()):
#     print(f'user key {user_data[0]} with value {user_data[1]} has index {index}')
# #
# # for index, user_key, user_value in enumerate(user.items()):
# #     print(f'user key {user_key} with value {user_value} has index {index}')


def is_empty_row(row):
    return len(row) > 0

#
# my_descr = 'My name is  Den'.split(' ')
# print(my_descr)
#
# resl = list(filter(is_empty_row, my_descr))
# print(resl)

# res = []
# for el in my_descr:
#     if is_empty_row(el):
#         res.append(el)
#
# res = [k for k in my_descr if is_empty_row(k)]

# def multiply_n(number):
#     return number*5
#
# res_map = list(map(multiply_n, range(10, 20)))
# print(res_map)
#
# res = []
# for k in range(10, 20):
#     res.append(multiply_n(k))
# print(res)
# res = [multiply_n(k) for k in range(10, 20)]
# print(res)

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = ['a', 'b', 'c']
# zipped = zip(list1, list2)
# print(dict(zipped))
#
# my_dict = dict([('a', 1), ('b', 2)])
# print(my_dict)


# isinstance()
# type()

my_str = '123'
my_int = 123
my_bool = True

# print(f'my_int {my_int} is int: {isinstance(my_int, int)}')  # True
# print(f'my_str {my_str} is int: {isinstance(my_str, int)}')  # False
# print(f'{{1:2}} is dict: {isinstance({1:2}, dict)}')  # True
#
# print(f'my_str {my_str} has type {type(my_str)}')
# print(f'my_str {my_str} is str: {type(my_str) is str}')
#
# print(f'[1,23] is list: {type([1,23]) is list}')
# print(f'[1,23] : {type([1,23])}')

# print(isinstance(True, int))  # невірно
# print(type(True) is int)  # вірно
# print(type(True))





