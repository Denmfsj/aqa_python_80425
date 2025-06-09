from xmlrpc.client import Boolean

db_response = {'user_id': 1, 'name': 'Den', 'courses': ['math', 'lit']}


class DbUser:

    def __init__(self, user_id, name, courses):

        self.user_id = user_id
        self.name = name
        self.courses = courses


    def __setattr__(self, key, value):

        if key == 'user_id' and value <= 0:
            raise AttributeError('User_id should be > 0')

        if key == 'name' and len(value) == 0:
            raise  AttributeError('name should be not empty string')

        if key == 'courses' and type(value) is not list:
            raise  AttributeError('courses should be list')

        super().__setattr__(key, value)  # встановлюємо значення value для атрибуту key


    def set_age(self, number):
        self.age = number

    def __str__(self):
        return f'user_id = {self.user_id}, user_name = {self.name}'


user = DbUser(**db_response)
print(user)
set_age = 15
user.user_id = 0
print(user)
