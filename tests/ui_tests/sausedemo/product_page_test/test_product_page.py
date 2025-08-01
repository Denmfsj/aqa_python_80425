import time

import pytest

from core.UI.enum.product_sort_enum import ProductSortEnum
from core.UI.locators.products_page_locators import ProductsPageLocators
from core.UI.pages.products_page import ProductsPage


def test_product_page_has_n_product_cards(products_page, driver):
    """ # фікстура
        #  - Відрити сторінку,
        #  - залогінитись,

        #  - знайти всі картки(продукти): знайти локатор і записати це в ProductPage класс
        #  - порахувати, що їх 6
        """

    products_page.get_product_cards()


@pytest.mark.parametrize('sort_value, is_reverse',
                         [
                             (ProductSortEnum.HIGH_2_LOW.value, True),
                             (ProductSortEnum.LOW_2_HIGH.value, False),
                         ], ids=["price desc", "price asc"])
def test_product_page_sorting_by_price(products_page, sort_value, is_reverse):


    #  відсортував по ціні (high > low)
    products_page.sort_by_value(sort_value)

    prices = products_page.get_product_prices()

    prices_float = [float(p[1:]) for p in prices] # p[1:] - вікине знак долара, float(p[1:]) - перетворить на float
    sorted_prices = sorted(prices_float, reverse=is_reverse) # створюю новий список який додатково відсотований від більшого до меньшого

    assert sorted_prices == prices_float, 'Prices are not sorted'


@pytest.mark.parametrize('sort_value, is_reverse',
                         [
                             (ProductSortEnum.default_value(), False),
                             (ProductSortEnum.NAME_A_Z.value, False),
                             (ProductSortEnum.NAME_Z_A.value, True),
                         ],
                         ids=["Default sorting", "Name asc", "Name desc"]
                         )
def test_product_page_sorting_by_name(products_page, sort_value, is_reverse):


    #  відсортував по ціні (high > low)
    products_page.sort_by_value(sort_value)

    names = products_page.get_product_names()

    sorted_names = sorted(names, reverse=is_reverse)

    assert sorted_names == names, 'Names are not sorted'






