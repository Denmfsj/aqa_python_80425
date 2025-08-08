import random

import allure

from core.UI.enum.product_add_to_card_tests import ProductAddCardText


@allure.epic('Sause demo site')
@allure.feature('Product actions')
@allure.story('basket actions')
def test_product_page_add_and_remove_product_from_card(products_page, driver):


    products_page.get_product_cards()

    product_number = random.choice(range(1,7))  # продукти 1 - 6
    print('product_number is', product_number)


    base_text = products_page.get_text_button_by_product_number(product_number)

    assert base_text == ProductAddCardText.ADD.value, \
        f'Expected test is {ProductAddCardText.ADD.value} but actual is {base_text}'



    products_page.click_button_by_product_number(product_number)

    base_text = products_page.get_text_button_by_product_number(product_number)

    assert base_text == ProductAddCardText.REMOVE.value, \
        f'Expected test is {ProductAddCardText.REMOVE.value} but actual is {base_text}'

    assert products_page.get_number_of_products_in_bucket() == 1


    products_page.click_button_by_product_number(product_number)
    base_text = products_page.get_text_button_by_product_number(product_number)

    assert base_text == ProductAddCardText.ADD.value, \
        f'Expected test is {ProductAddCardText.ADD.value} but actual is {base_text}'

    assert  products_page.get_number_of_products_in_bucket() == 0




