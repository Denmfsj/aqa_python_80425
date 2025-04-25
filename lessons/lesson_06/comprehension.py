# my_list_of_sq = []
# for k in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
#     if k % 2 == 0:  #  якщо парне число
#         my_list_of_sq.append(k**2)  # додати до списка квадрат числа
#
# print(my_list_of_sq)

# [змінна_яку_додати for змінна_яку_додати in iterable_onject if condition]
# my_list_of_sq_list_comprehension_all_numbers = [k**2 for k in range(1, 10)]
# my_list_of_sq_list_comprehension = [k**2 for k in range(1, 10) if k % 2 == 0]
# print(my_list_of_sq_list_comprehension_all_numbers)
# print(my_list_of_sq_list_comprehension)

# api_response = [1, 2, 4, 1,  None, 0, '', 5, 'Den']
#
# # all_not_empty_values = [k for k in api_response if k]  # всі елементи для яких bool(k) == True
# # print(all_not_empty_values)
#
# all_numbers = [k for k in api_response if type(k) == int]
# print(all_numbers)
#
# all_numbers_set = {k for k in api_response if type(k) == int}
# print(all_numbers_set)

# all_not_empty_strings = [k for k in api_response if type(k) == str and len(k) > 0]
# print(all_not_empty_strings)


my_list_of_names = ['Den', 'Alex', 'Sofia', 'Alex', 'Ivan']

# словник з довжиною імен

# my_dict_with_len_of_names = {}
#
# for name in my_list_of_names:
#     my_dict_with_len_of_names[name] = len(name)
#
# print(my_dict_with_len_of_names)

my_dict_with_len_of_names = {name: len(name) for name in  my_list_of_names}
print(my_dict_with_len_of_names)

