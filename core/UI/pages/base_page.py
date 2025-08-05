from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.UI.locators.login_page_locators import LoginPageLocators
from core.UI.utils.custom_wait import WaitNElements


class BaseElements:

    def __init__(self, driver):
        self._driver = driver

    def _visible_element(self, locator, timeout=2, message=None):
        el = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator), message=message)
        return el

    def _visible_elements(self, locator, timeout=2, message=None):
        els = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_all_elements_located(locator), message=message)
        return els


    def _button_clickable(self, locator, timeout=2, message=None):
        el = WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(locator),
               message=message)
        return el

    def wait_n_elements(self,  locator, quantity_of_els, timeout=2, message=None):
        el = WebDriverWait(self._driver, timeout
                           ).until(WaitNElements(locator=locator, quantity=quantity_of_els),
               message=message)

        return el


class BasePage(BaseElements):

    def __init__(self, driver, url):
        self.url = url
        super().__init__(driver=driver)


    def open_page(self):
        self._driver.get(self.url)
        return self
