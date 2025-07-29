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


def test_login_ring_user_name_negative(driver, user_creds, login_page, product_page):

    # fixture
    user_name, password = user_creds

    login_page.open_page()
    login_page.set_user_pwd(password).set_user_name('test_wrong_user_name').click_login_button()

    #  Тут я вже буду шукати, якщо нема - буде помилка
    login_page.check_red_cross_are_present()

    time.sleep(1)