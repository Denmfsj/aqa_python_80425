

my_var = (1)
my_tuple = (1,)
my_tuple2 = (1,2)
my_tuple3 = 'den', 'alex', 'mor'

# print(type(my_var), my_var)
# print(type(my_tuple), my_tuple)
# print(type(my_tuple2), my_tuple2)
# print(type(my_tuple3), my_tuple3)
#
# print(my_tuple3[0])
# print(my_tuple3[1])
# print(my_tuple3[1:])


tuple_with_diff_types = (1, 2.02, 'Den', None, True, (1,2,3, f'{2 + 8}asd'), [1,2,34,4])

# print(type(tuple_with_diff_types[1]))
# print(type(tuple_with_diff_types[2]))
# print(type(tuple_with_diff_types[-2]))
# print(tuple_with_diff_types[-2])
# print(type(tuple_with_diff_types[-1]))

list_in_tuple = tuple_with_diff_types[-1]

# print(id(tuple_with_diff_types), 'tuple_id')
# print(id(list_in_tuple))
# print(id(tuple_with_diff_types[-1]))

list_in_tuple.append('last_el')  # додав 1 елемент в список
# print(list_in_tuple)
# print(tuple_with_diff_types)
# print(id(tuple_with_diff_types), 'tuple_id')

# tuple_with_diff_types = tuple_with_diff_types[:2]
# print(id(tuple_with_diff_types), 'tuple_id')
# print(tuple_with_diff_types)

# tuple_with_diff_types = (1, 2.02, 'Den', None, True, (1,2,3, f'{2 + 8}asd'), [1,2,34,4])
# print(tuple_with_diff_types[-1][2])

my_name = 'Den'
my_age = 33
my_name_as_a_tuple = tuple(my_name)  # my_name повинно бути ітерабельним
print(my_name_as_a_tuple)

# my_name_as_a_tuple = tuple(1)

my_friends = ['None', 'Oleh']  # list, mutable

# print('my_friends', id(my_friends))
tuple_of_vars = (my_name, my_age, 33, 35, 33, my_name_as_a_tuple, my_friends)
# print(tuple_of_vars)

my_friends.append('Nick')  # зміню my_friends: додам 1 ім'я
# print('my_friends', id(my_friends))
my_name = 'Oleh'
# print(tuple_of_vars)
#
#
# print(tuple_of_vars.count(['None', 'Oleh', 'Nick']))
# print(tuple_of_vars.count('Nick'))


print(tuple_of_vars.index(33, 3, 4))

# iterable
# list, dict, tuple, set, str
# MAX_AGE = 99
# MIN_AGE = 6
# AGE_TUPLE = (99, 6)  # max and min age




