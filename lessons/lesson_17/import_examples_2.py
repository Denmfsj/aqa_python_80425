import json
import os

from lessons.lesson_17.import_examples import (BaseCarClass, FakeCar,
                                               Honda)
from lessons.lesson_17.import_examples import class_cars

# ctrl/command(для мака) + alt + o

if __name__ == '__main__':

    my_nissan = class_cars.Nissan('v4')
    my_honda = Honda('v4')
    my_base_car = BaseCarClass('v8')
    my_fake_car = FakeCar()

    b = os.system
    a = json.load


    # print(os.path.abspath(__file__))
    #
    # print(my_nissan.possible_models)
    # print(my_honda.brand)
    # print(my_base_car.engine)
    # print(my_fake_car.is_real)

    print(dir([1,2,3]))


# print(class_cars.nissan_zd30)

# print(test_functions.factorial(5))