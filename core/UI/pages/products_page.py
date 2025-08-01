from typing import List

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

from core.UI.locators.products_page_locators import ProductsPageLocators
from core.UI.pages.base_page import BasePage
from utils.settings import d_settings


class ProductsPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/inventory.html'):
        super().__init__(driver, url)


    def check_page_is_loaded(self):

        assert self._driver.current_url == self.url, \
            f"Current urls must be {self.url} but it is {self._driver.current_url}"

        (WebDriverWait(self._driver, 5).
         until(EC.presence_of_element_located(ProductsPageLocators.inventory_list_loc),
               message='Cant find product list on Product Page'))


    def get_product_cards(self, expected_count_of_products=None) -> list:

        if expected_count_of_products is None:
            expected_count_of_products = d_settings.count_of_product_cards

        return self.wait_n_elements(
            locator=ProductsPageLocators.product_card_loc,
            quantity_of_els=expected_count_of_products, timeout=3,
            message=f'Cant find {expected_count_of_products} product cards on Product page')


    def sort_by_value(self, value):
        select = Select(self._driver.find_element(*ProductsPageLocators.sorting_select_loc))
        select.select_by_value(value)
        return self

    def get_product_prices(self) -> List[str]:
        els = self._visible_elements(locator=ProductsPageLocators.product_price_loc,
                                        timeout=2, message='Cant find any price on Product page')

        return [el.text for el in els] # el.text - витягне "$49.99"

    def get_product_names(self) -> List[str]:
        els = self._visible_elements(locator=ProductsPageLocators.product_name_loc,
                                        timeout=2, message='Cant find any name on Product page')

        return [el.text for el in els]

    def click_button_by_product_number(self, product_number: int):
        els = self._visible_elements(locator=ProductsPageLocators.product_button_loc,
                                     timeout=2, message='Cant find any button on Product page')

        el = els[product_number - 1]
        el.click()

        return self


    def get_text_button_by_product_number(self, product_number: int) -> str:
        els = self._visible_elements(locator=ProductsPageLocators.product_button_loc,
                                     timeout=2, message='Cant find any button on Product page')

        return els[product_number - 1].text


    def get_number_of_products_in_bucket(self) -> int:

        try:
            el = self._visible_element(locator=ProductsPageLocators.shopping_card_bange,
                                         timeout=2, message='Cant find Backet number')
        except Exception as e:
            return 0

        return int(el.text)