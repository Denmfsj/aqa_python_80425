#
# # список прав
# response = [
#     {'id': 1, 'name': 'read_only', 'descriptions': 'For all users'},
#     {'id': 2, 'name': 'RW', 'descriptions': 'For writing and reading'},
#     {'id': 3, 'name': 'delete', 'descriptions': 'For deleting'},
#     {'id': 3, 'name': 'delete', 'descriptions': 'For deleting'},
#     {'id': 4, 'name': 'all', 'descriptions': 'For Admins'},
#     {'id': None, 'name': 'broken', 'descriptions': None},
# ]

users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
]

# for user in users:
#     user_job = user.get('job')
#     if user.get('job'):#  is not None:   # is None, is False, is True
#
#         for job in user_job:
#             print(f'{user.get("name")} is a/an {job.get("title")}')


# for number in range(1, 5):  # for number in (1,2,3,4)
#     for number_2 in range(5, 10): # for number_2 in (5,6,7,8,9)
#
#         print(f'{number}*{number_2}={number*number_2}')
