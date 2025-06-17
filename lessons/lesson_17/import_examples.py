# import pytest
#
# import sys

# sys.path.append('/home/den/hillel/aqa_python_80425/utils')
#
# import test_functions

from utils import test_functions

from lessons.lesson_14 import class_cars
from lessons.lesson_14.class_cars import Honda
# from lessons.lesson_14.class_cars import *  # import все

from lessons.lesson_14.class_cars import Car as BaseCarClass
from lessons.lesson_14.classes_instances import Car as FakeCar

import os.path


__all__ = ['FakeCar', 'BaseCarClass']

if __name__ == '__main__':

    my_nissan = class_cars.Nissan('v4')
    my_honda = Honda('v4')
    my_base_car = BaseCarClass('v8')
    my_fake_car = FakeCar()

    # print(os.path.abspath(__file__))
    #
    # print(my_nissan.possible_models)
    # print(my_honda.brand)
    print(my_base_car.engine)
    print(my_fake_car.is_real)


# print(class_cars.nissan_zd30)

# print(test_functions.factorial(5))