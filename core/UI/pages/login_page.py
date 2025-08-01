from core.UI.locators.login_page_locators import LoginPageLocators
from core.UI.pages.base_page import BasePage
from core.UI.pages.products_page import ProductsPage
from utils.settings import d_settings


class LoginPage(BasePage):


    def __init__(self, driver, url=d_settings.sause_demo_url):
        super().__init__(driver, url)


    def set_user_name(self, user_name):

        user_name_input = self._visible_element(locator=LoginPageLocators.user_name_input_loc,
                                                timeout=1, message='Cant find username input on Login Page')
        user_name_input.send_keys(user_name)
        return self


    def set_user_pwd(self, user_pwd):
        password_input = self._visible_element(locator=LoginPageLocators.password_input_loc,
                                               message='Cant find password input on Login Page')

        password_input.send_keys(user_pwd)
        return self


    def click_login_button(self):
        self._button_clickable(locator=LoginPageLocators.login_button_loc,
                               message='Cant find/click login button on Login Page').click()
        return self


    # positive case
    def login(self, user_name, user_password) -> ProductsPage:
        self.set_user_name(user_name).set_user_pwd(user_password)
        self.click_login_button()

        product_page_instance = ProductsPage(self._driver)

        return product_page_instance

    def check_red_cross_are_present(self):

        self.wait_n_elements(locator=LoginPageLocators.red_cross, quantity_of_els=3,  timeout=3,
                    message='Cant find 3 red crosses on Login Page')
