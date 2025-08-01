import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from core.UI.pages.login_page import LoginPage
from core.UI.pages.products_page import ProductsPage
from utils.settings import d_settings


@pytest.fixture(scope='session')
def user_creds():
    user_name = d_settings.user_name
    password = d_settings.user_pwd
    yield user_name, password

@pytest.fixture(scope='package')
def driver() -> webdriver:

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='package')
def products_page(driver, user_creds) -> ProductsPage:
    name, pwd = user_creds
    return LoginPage(driver=driver).open_page().login(user_name=name, user_password=pwd)
