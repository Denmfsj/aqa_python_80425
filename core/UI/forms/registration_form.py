from core.UI.locators.login_page_locators import LoginPageLocators
from core.UI.pages.base_page import BaseElements


class RForm(BaseElements):


    def set_user_name(self, user_name):
        user_name_input = self._visible_element(locator=LoginPageLocators.user_name_input_loc,
                                                timeout=1, message='Cant find username input on Login Page')
        user_name_input.send_keys(user_name)

        return self