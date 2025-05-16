import unittest

import sys
import pathlib

path_to_base_folder = str(pathlib.Path(__file__).parent.parent.parent.parent)
sys.path.insert(0, path_to_base_folder)


from utils.test_functions import factorial



class FactorialNegativeTest(unittest.TestCase):


    def test_factorial_with_str(self):

        with self.assertRaises(TypeError):  # очікувати САМЕ TypeError і це буде позитивним результатом
            factorial('5')



if __name__ == '__main__': # якщо цей файл запущено
    unittest.main()