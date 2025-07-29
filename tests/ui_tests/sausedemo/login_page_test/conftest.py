import pytest
from selenium import webdriver

from core.UI.pages.login_page import LoginPage
from core.UI.pages.products_page import ProductsPage


@pytest.fixture
def driver() -> webdriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def user_creds():
    user_name = "standard_user"
    password = "secret_sauce"
    yield user_name, password

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def product_page(driver):
    return ProductsPage(driver=driver)
