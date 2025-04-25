# my_data = {
#     'id': 11,
#     'name': 'Den',
#
#     'work_info': {
#         'id': 78,
#         'position': 'AQA',
#         # 'skills': {'id': 5, 'value': 'Python'}
#         'skills': [{'id': 5, 'value': 'Python'}, {'id': 8, 'value': 'git'}]
#     },
# }

# print(my_data['id'])
# print(my_data.get('id'))
# print(my_data.get('id1'))
# print(my_data.get('id1', 'unknown'))

# my_data['new_key'] = 'New field'
# print(my_data)
# my_data['new_key'] = 'super new field'
# print(my_data)
#
# print(my_data)
# my_data.clear()  # поверне породжінй словник
# print(my_data)

# some_sub_dict = {'country': 'Ukraine', 'phone': '38093'}
# my_data.update(some_sub_dict)  # по'єднати 2 словника
# print(my_data['country'])
# print(my_data)

# видалення данних з словника
# print(my_data.pop('work_info'))
# print(my_data)
# print(my_data.popitem())
# print(my_data)

# print(my_data.pop('work_info1', 'asd')) якщо нема ключа work_info1 то поверни asd
# print(my_data)

#
# my_data.pop('name')
# my_data.pop('phone')

my_data = {
    'id': 11,
    'name': 'Den',

    'work_info': {
        'id': 78,
        'position': 'AQA',
        # 'skills': {'id': 5, 'value': 'Python'}
        'skills': [{'id': 5, 'value': 'Python'}, {'id': 8, 'value': 'git'}]
    },
}

my_data['phone'] = '123456'

# copy_of_my_data = my_data.copy()  # поверхнева копія
import copy

# copy_of_my_data = copy.deepcopy(my_data)  # повноцінна копія
#
# my_data['phone'] = '9999999'
# my_data['work_info']['skills'] = []
# print(my_data)
# print(copy_of_my_data)

# my_list = [1,2, [3,4, {'some_key': 'some_value'}]]
#
# # copy_of_list = my_list[:]  # copy via slise, поверхнева копія
# # copy_of_list = my_list.copy()  # поверхнева копія
# copy_of_list = copy.deepcopy(my_list)  # повноцінна копія
# my_list[2][2] = {}
#
# print(my_list)
# print(copy_of_list)


my_list_of_names = ['Den', 'Alex', 'Sofia', 'Alex', 'Ivan']

dict_with_numbers_of_names = {}

# for name in my_list_of_names:
#     len_of_name = len(name)
#
#     if len_of_name not in dict_with_numbers_of_names:  # if len_of_name not in dict_with_numbers_of_names.keys()
#         dict_with_numbers_of_names[len_of_name] = 0
#
#     value = dict_with_numbers_of_names[len_of_name]
#     value = value +1
#     dict_with_numbers_of_names[len_of_name] = value

    # dict_with_numbers_of_names[len_of_name] += 1  # a += b  === a = a + b

# for name in my_list_of_names:
#     len_of_name = len(name)
#
#     # if len_of_name not in dict_with_numbers_of_names:  # if len_of_name not in dict_with_numbers_of_names.keys()
#     #     dict_with_numbers_of_names[len_of_name] = 0
#
#     # поверни значення по ключу АБО 0(тоді запиши 0 як значення по ключу в словник)
#     value = dict_with_numbers_of_names.setdefault(len_of_name, 0)
#
#     value = dict_with_numbers_of_names[len_of_name]
#     value = value + 1
#     dict_with_numbers_of_names[len_of_name] = value
#
# print(dict_with_numbers_of_names)

new_dict_from_list_of_tuples =  dict([
    (1, "alex"),
    (2, 'Ivan'),
    (3, 'Maria')
])

# int('1')
# list('asd')
# tuple([1,2,3])
# len('asd')
# type('asd')

# print(new_dict_from_list_of_tuples)

list_of_ids = [1,2,3,4,5,6,7,8]
list_of_positions = ['qa', 'aqa', 'pm']

print(dict(zip(list_of_ids, list_of_positions)))

dict_compr = {
    list_of_ids[i]: list_of_positions[i]
              for i in range(min(len(list_of_ids), len(list_of_positions)))}

print(dict_compr)