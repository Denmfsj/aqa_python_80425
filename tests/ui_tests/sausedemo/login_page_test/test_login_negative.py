import time

import allure

from tests.ui_tests.sausedemo.login_page_test.conftest import TestLogin


@allure.story('Negative test')
class TestLoginNegative(TestLogin):
    def test_login_ring_user_name_negative(self, driver, user_creds, login_page, product_page):

        # fixture
        user_name, password = user_creds

        login_page.open_page()
        login_page.set_user_pwd(password).set_user_name('test_wrong_user_name').click_login_button()

        #  Тут я вже буду шукати, якщо нема - буде помилка
        login_page.check_red_cross_are_present()

        time.sleep(1)