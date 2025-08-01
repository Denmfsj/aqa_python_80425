from selenium.webdriver.common.by import By


class ProductsPageLocators:

    inventory_list_loc = (By.CSS_SELECTOR, 'div.inventory_list')
    product_card_loc = (By.XPATH, '//div[@data-test="inventory-item"]')
    product_price_loc = (By.XPATH, '//div[@class="inventory_item_price"]')
    product_name_loc = (By.XPATH, '//div[@data-test="inventory-item-name"]')
    product_button_loc = (By.XPATH, '//div[@data-test="inventory-item"]//button')
    sorting_select_loc = (By.XPATH, '//select[@data-test="product-sort-container"]')
    shopping_card_bange = (By.XPATH, '//span[@data-test="shopping-cart-badge"]')
