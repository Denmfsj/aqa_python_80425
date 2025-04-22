pi_number = 3.14


# asd
#

my_data = {
    'id': 11,
    'name': 'Den',

    'work_info': {
        'id': 78,
        'position': 'AQA',
        # 'skills': {'id': 5, 'value': 'Python'}
        'skills': [{'id': 5, 'value': 'Python'}, {'id': 8, 'value': 'git'}]
    },
    False: 123,
    None: 123,
    10-82: 123,
    pi_number: 'pi',
    # 5: input('enter your age'),
    (1,2): 123,
    # input('enter your name'): 45
    # [1,2]: 123,
    # {1:2}: 123
}

work_info_data = my_data['work_info']  # dict
skills = work_info_data['skills']  # list
last_skill = skills[-1]  # dict
value_of_last_skill = last_skill['value']  # string

print(my_data['work_info']['skills'][-1]['value'])
print(my_data['work_info']['skills'][-1])
# print(work_info_data)
# print(work_info_data['id'])
# print(work_info_data['position'])
# print(work_info_data['skills'])
# print(work_info_data['skills'][-1])
# my_data['work_info']['skills'].append('QA')
# print(my_data['work_info']['skills'][-1])
# print(my_data)

# print(my_data)
# user_id = my_data.get('id', -1)  # id - це ключ
# user_name = my_data['name']  # name - це ключ
# # input_value = my_data['Den']
# # additional_info = my_data[(1,2)]
#
# print(user_id)
# print(user_name)
# print(additional_info)
# print(input_value)