api_response = {'id_': 1, 'name': 'Den', 'courses': ['math', 'lit'], 'average_score': 70}
db_response = {'id_': 1, 'db_name': 'Den', 'has_score': True, 'is_student': True}


class DbUser:
    def __init__(self, id_, db_name, has_score, is_student):
        self.user_id = id_
        self.name = db_name
        self.has_score = has_score
        self.is_student = is_student

class ApiUser:

    def __init__(self, id_, name, courses, average_score):
        self.user_id = id_
        self.name = name
        self.courses = courses
        self.average_score = average_score


list_of_equal_values = ['user_id', 'name']

api_u = ApiUser(**api_response)
db_u = DbUser(**db_response)
#
# assert api_u.user_id == db_u.user_id
# assert api_u.name == db_u.name

for field_name in list_of_equal_values:
    api_value =  getattr(api_u, field_name) # getattr(api_u, "user_id")
    print(f'api: {api_value}')
    print(f'db: {getattr(db_u, field_name)}')
    # assert getattr(api1, field_name) == getattr(api2, field_name)
    # api_u.__getattribute__('user_id')  == getattr(api_u, 'user_id')