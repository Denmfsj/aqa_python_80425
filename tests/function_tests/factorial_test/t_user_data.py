import unittest
import sys
import pathlib

path_to_base_folder = str(pathlib.Path(__file__).parent.parent.parent.parent)
sys.path.insert(0, path_to_base_folder)

from core.functions.factorials.assertations.assert_user_data_finct import assert_user_data

# data from db
user_data = [
    {'user_id': 1, 'name': 'den', 'companies': ['c1', 'c2', 'c3']},
    {'user_id': 2, 'name': 'alex', 'companies': ['c11', 'c12', 'c13']},
    {'user_id': 3, 'name': 'sofa', 'companies': ['c111', 'c112', 'c113']},
]


class FactorialNegativeTest(unittest.TestCase):


    def test_user_data_equal_user_base(self):

        expected_user_id = 1

        actual_result = [k for k in user_data if k['user_id'] == expected_user_id][0]
        expected_result = {'user_id': 1, 'name': 'den', 'companies': ['c1', 'c2', 'c3']}

        self.assertEqual(expected_result, actual_result)


    def test_user_data_equal_user_with_details(self):
        """
        test that checks that expected data from user is equal to actual data from db
        checking id, name and companies fields
        """

        expected_user_id = 1

        actual_result = [k for k in user_data if k['user_id'] == expected_user_id][0]
        expected_result = {'user_id': 1, 'name': 'den', 'companies': ['c1', 'c2', 'c3']}

        assert_user_data(act=actual_result, exp=expected_result)




    def test_diff_types_of_asserts(self):

        user_name = None
        company_score = 59.5

        self.assertNotEqual(1, 2, msg='Some custom error description')
        self.assertIsNone(user_name, msg='Data from db should be None')
        self.assertIsNotNone([], msg='Data from api /asd/asd/user/2')

        self.assertIn(5, [1,2,5,3,8], msg='5 mut be in')
        self.assertNotIn(2, [1,3,8], msg='2 mut be NOT in')

        self.assertAlmostEqual(company_score, 60, delta=1)

        self.assertGreaterEqual(5, 5)


    # def test_only_letters(self):
    #
    #     user_name = 'Alex'
    #
    #     res = re.findall(r'[A-Z]', user_name)
    #
    #     pass

if __name__ == '__main__': # якщо цей файл запущено
    unittest.main()