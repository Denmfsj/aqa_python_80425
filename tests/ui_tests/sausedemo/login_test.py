from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


def test_login_standart_user():

    url = "https://www.saucedemo.com/"
    user_name = "standard_user"
    password = "secret_sauce"

    driver = Chrome()
    driver.get(url)


    user_name_input = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    password_input = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    login_button = driver.find_element(By.ID, 'login-button')

    user_name_input.send_keys(user_name)
    password_input.send_keys(password)
    login_button.click()

    #  Тут я вже буду шукати, якщо нема - буде помилка
    # driver.find_element(By.CSS_SELECTOR, 'div.inventory_list')

    time.sleep(1)