import unittest

import sys
import pathlib

import pytest

path_to_base_folder = str(pathlib.Path(__file__).parent.parent.parent.parent)
sys.path.insert(0, path_to_base_folder)


from utils.test_functions import factorial



class FactorialPositiveTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Sending request to some endpoint .................')
        cls.user_id = 6 # посилаємо запит на api ендпоінт і отримаємо це значення

    @classmethod
    def tearDownClass(cls):
        print('Smth after all tests were done')

    # def setUp(self):
    #     print('Do smth BEFORE each test')
    #
    #
    # def tearDown(self):
    #     print('Do smth AFTER each test')


    def test_factorial_with_5(self):

        actual_result = factorial(5)
        expected_result = 120

        # print('test_factorial_with_5 is running')

        self.assertEqual(6, self.user_id)
        self.assertEqual(expected_result, actual_result)


    def test_factorial_with_0(self):

        actual_result = factorial(0)
        expected_result = 1

        # print('test_factorial_with_0 is running')

        self.assertEqual(6, self.user_id)
        self.assertEqual(expected_result, actual_result)


@pytest.mark.parametrize(
    'input_data, expected',
    [
        (0, 1),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
        (5, 120),
    ]
)
def test_factorial_with_5(input_data, expected):

    actual_result = factorial(input_data)
    assert actual_result == expected




if __name__ == '__main__': # якщо цей файл запущено
    unittest.main(verbosity=2)