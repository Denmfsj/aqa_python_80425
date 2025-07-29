import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.UI.locators.login_page_locators import LoginPageLocators
from core.UI.locators.products_page_locators import ProductsPageLocators
from core.UI.pages.login_page import LoginPage
from core.UI.pages.products_page import ProductsPage




def test_login_standard_user(driver, user_creds, login_page):

    # fixture
    user_name, password = user_creds

    login_page.open_page()
    product_page = login_page.login(user_name=user_name, user_password=password)

    #  Тут я вже буду шукати, якщо нема - буде помилка
    product_page.check_page_is_loaded()


    time.sleep(1)

