users = (
    {'id': 1, 'name': 'Anex'},
    {'id': 2, 'name': 'Alex'},
    {'id': 3, 'name': 'Youri'},
    {'id': 5, 'name': 'Den'},
    {'id': None, 'name': 'Den'},
    {'id': 8, 'name': True},
)

import json

# print(users)
# json_users = json.dumps(users, indent=2)
# print(json_users)
# print(type(json_users))

# with open('user.json', 'w') as f:
#     json.dump(users, f, indent=4)
#
# with open('user2.json', 'w') as f:
#     f.write(json_users)

with open('user.json') as f:
    data_str = f.read()

data_json = json.loads(data_str)

print(type(data_json))
print(data_json)