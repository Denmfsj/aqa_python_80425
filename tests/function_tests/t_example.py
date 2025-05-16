import unittest



class MyTest(unittest.TestCase):


    def test_example(self):

        result = 'hello'
        expected_result = 'hello'

        assert expected_result == result


    def test_example_second(self):

        result = 'hello'
        expected_result = 'hello1'

        assert expected_result == result, f'expected if {expected_result} but actual is {result}'

        # if expected_result != result:
        #     raise AssertionError(f'expected if {expected_result} but actual is {result}')


if __name__ == '__main__': # якщо цей файл запущено
    print('Test gonna started ')
    unittest.main()