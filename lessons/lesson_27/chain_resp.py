from faker import Faker
import random

class UserInfo:

    faker = Faker()

    def __init__(self, name=None, age=None, position=None):

        self.name=name
        self.age=age
        self.position=position

    def with_random_name(self):
        self.name = self.faker.name()
        return self

    def with_random_age(self):
        self.age = random.choice(range(18, 66))  # від 18 до 65 включно
        return self

    def with_random_position(self):
        self.position = self.faker.job()
        return self

    def __str__(self):
        return f'{self.name}, {self.age}, {self.position}'

den = UserInfo()

print(den)
den.name = 'Den'
print(den)
den.with_random_age().with_random_position().with_random_name()
print(den)

den2 = den.with_random_position()
den2.with_random_age()
print(id(den))
print(id(den2))

print(den)
print(den2)

