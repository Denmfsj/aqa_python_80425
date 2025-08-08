import time

import allure

from tests.ui_tests.sausedemo.login_page_test.conftest import TestLogin


@allure.story('Login page')
class TestSauseDemoLogin(TestLogin):
    def test_login_standard_user(self, driver, user_creds, login_page):

        # fixture
        user_name, password = user_creds

        login_page.open_page()
        product_page = login_page.login(user_name=user_name, user_password=password)

        #  Тут я вже буду шукати, якщо нема - буде помилка
        product_page.check_page_is_loaded()


        time.sleep(1)

