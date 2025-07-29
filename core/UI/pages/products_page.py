from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.UI.locators.products_page_locators import ProductsPageLocators
from core.UI.pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/inventory.html'):
        super().__init__(driver, url)


    def check_page_is_loaded(self):

        assert self._driver.current_url == self.url, \
            f"Current urls must be {self.url} but it is {self._driver.current_url}"

        (WebDriverWait(self._driver, 5).
         until(EC.presence_of_element_located(ProductsPageLocators.inventory_list_loc),
               message='Cant find product list on Product Page'))
