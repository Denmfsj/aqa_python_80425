from datetime import datetime

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import UI_SCREENSHOTS_FOLDER
from core import *
from utils.settings import d_settings


@allure.epic('Sause demo site')
@pytest.mark.ui_test
class SauseDemoBase:
    pass

@pytest.fixture(scope='session')
def user_creds():
    user_name = d_settings.user_name
    password = d_settings.user_pwd
    yield user_name, password


@pytest.fixture
def driver() -> webdriver:

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.browser_version = "114"

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='package')
def driver_package() -> webdriver:

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.browser_version = "114"

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='module')
def login_page_negative_tests(driver_package):

    return LoginPage()

@pytest.fixture
def product_page_package(driver_fn):
    return UI_LoginPage(driver=driver_fn).open_page().login(user_name=name, user_password=pwd)


@pytest.fixture(scope='package')
def products_page(driver, user_creds) -> UI_ProductPage:
    name, pwd = user_creds
    return UI_LoginPage(driver=driver).open_page().login(user_name=name, user_password=pwd)


@pytest.fixture(autouse=True)
def take_screenshot_after_test(request, driver):
    yield
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{UI_SCREENSHOTS_FOLDER}/{test_name}_{timestamp}.png"
    UI_SCREENSHOTS_FOLDER.mkdir(exist_ok=True)
    driver.save_screenshot(filename)

    # приклріпляю файл до репорта
    with open(filename, 'rb') as f:
        file_read_bytes = f.read()

    allure.attach(file_read_bytes, name=filename, attachment_type=allure.attachment_type.PNG)
