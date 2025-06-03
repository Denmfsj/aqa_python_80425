class Car:

    number_of_wheels = 0  # TODO: delete old hardcoded value

    def __init__(self, engine, number_of_wheels=4):
        self.engine = engine
        self.number_of_wheels = number_of_wheels


class Nissan(Car):
    number_of_wheels = 10
    brand = 'Nissan'

    possible_engines = ['v4', 'v8']
    possible_models = ['y61', 'z30', 'Navara']

    @classmethod
    def get_all_possible_models(cls):

        return f"{cls.brand}: {str(cls.possible_models)}"


class Honda(Car):
    possible_engines = ['v4', 'v6']
    brand = 'Honda'


nissan_zd30 = Nissan('v4')
nissan_td48 = Nissan('v8', number_of_wheels=8)
# h_civic = Honda('v8')

nissan_zd30.possible_engines.append('v10')
print(Nissan.brand)
print(Nissan.possible_models)
print(Nissan.get_all_possible_models())

print(nissan_td48.get_all_possible_models())

# print(nissan_zd30.possible_engines)
# print(nissan_td48.possible_engines)
# Car.number_of_wheels = 16
# print(nissan_td48.number_of_wheels)
# nissan_td48.brand = 'y61'
# print(nissan_td48.brand)
# print(nissan_td48.__class__.brand)





# print(Nissan.brand)
#
# nissan_td48.brand = 'V222'
#
# print(nissan_zd30.brand)
# print(nissan_td48.brand)
#
# Nissan.brand = 'Nissan v2'
#
# print(nissan_zd30.brand)
# print(nissan_td48.brand)
# print(Nissan.brand)