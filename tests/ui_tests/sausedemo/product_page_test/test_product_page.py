import allure
import pytest

from core.UI.enum.product_sort_enum import ProductSortEnum
from tests.ui_tests.sausedemo.conftest import SauseDemoBase


@allure.feature('Product actions')
class TestProduct(SauseDemoBase):

    @allure.story('Product of default values')
    def test_product_page_has_n_product_cards(self, products_page, driver):
        """ # фікстура
            #  - Відрити сторінку,
            #  - залогінитись,

            #  - знайти всі картки(продукти): знайти локатор і записати це в ProductPage класс
            #  - порахувати, що їх 6
            """

        products_page.get_product_cards()



    @allure.story('Sorting')
    @pytest.mark.parametrize('sort_value, is_reverse',
                             [
                                 (ProductSortEnum.HIGH_2_LOW.value, True),
                                 (ProductSortEnum.LOW_2_HIGH.value, False),
                             ], ids=["price desc", "price asc"])
    def test_product_page_sorting_by_price(self, products_page, sort_value, is_reverse):


        #  відсортував по ціні (high > low)
        products_page.sort_by_value(sort_value)

        prices = products_page.get_product_prices()

        prices_float = [float(p[1:]) for p in prices] # p[1:] - вікине знак долара, float(p[1:]) - перетворить на float
        sorted_prices = sorted(prices_float, reverse=is_reverse) # створюю новий список який додатково відсотований від більшого до меньшого

        assert sorted_prices == prices_float, 'Prices are not sorted'

    @allure.story('Sorting')
    @pytest.mark.ui_test
    @pytest.mark.parametrize('sort_value, is_reverse',
                             [
                                 (ProductSortEnum.default_value(), False),
                                 (ProductSortEnum.NAME_A_Z.value, False),
                                 (ProductSortEnum.NAME_Z_A.value, True),
                             ],
                             ids=["Default sorting", "Name asc", "Name desc"]
                             )
    def test_product_page_sorting_by_name(self, products_page, sort_value, is_reverse):


        #  відсортував по ціні (high > low)
        products_page.sort_by_value(sort_value)

        names = products_page.get_product_names()

        sorted_names = sorted(names, reverse=is_reverse)

        assert sorted_names == names, 'Names are not sorted'






