import pytest
import allure
from selenium import webdriver

from core.UI.pages.login_page import LoginPage
from core.UI.pages.products_page import ProductsPage
from tests.ui_tests.sausedemo.conftest import SauseDemoBase

@allure.feature('Login actions')
class TestLogin(SauseDemoBase):
    pass


@pytest.fixture
def driver() -> webdriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def product_page(driver):
    return ProductsPage(driver=driver)
