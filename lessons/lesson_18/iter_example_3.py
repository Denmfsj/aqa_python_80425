from faker import Faker
import random


class DbGetter:
    """
    Class for getting n users from DB
    """

    def __init__(self, number_of_user):
        self.number_of_user = number_of_user
        self.__current_user = 1
        self.f = Faker()

    def __iter__(self):
        return self

    def __next__(self):

        # print('Getting data from DB')
        if self.__current_user < self.number_of_user:
            self.__current_user += 1
            return {
                'id': random.choice(range(18, 66)), # випадковий вік від 18 до 65
                'name': self.f.name()  # випадкове ім'я
            }
        raise StopIteration


for user in DbGetter(5):
    print(user)