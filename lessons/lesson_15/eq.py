# __eq__ котрий відповідає за порівняння

api_response = {'id_': 1, 'name': 'Den', 'courses': ['math', 'lit'], 'average_score': 70}
db_response = {'id_': 1, 'db_name': 'Den', 'has_score': True, 'is_student': True}


# assert api_response['id'] == db_response['id']
# assert api_response['name'] == db_response['db_name']

class DbUser:
    def __init__(self, id_, db_name, has_score, is_student):
        self.user_id = id_
        self.db_name = db_name
        self.has_score = has_score
        self.is_student = is_student

class ApiUser:

    def __init__(self, id_, name, courses, average_score):
        self.user_id = id_
        self.name = name
        self.courses = courses
        self.average_score = average_score


    def __eq__(self, other):

        # if isinstance(other, DbUser):
        #     other_name = other.db_name
        # else:
        #     other_name = other.name

        other_name = other.db_name if isinstance(other, DbUser) else other.name

        if self.user_id != other.user_id:
            return False
        if self.name != other_name:
            return False
        return True

api_u = ApiUser(**api_response)
db_u = DbUser(**db_response)
print(api_u == db_u)  # api_u.__eq__(db_u)
print(api_u == api_u)  #

api_u != db_u  # not(api_u == db_u)  not api_u.__eq__(db_u)