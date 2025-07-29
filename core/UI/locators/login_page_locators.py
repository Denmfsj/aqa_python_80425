from selenium.webdriver.common.by import By

class LoginPageLocators:

    user_name_input_loc = (By.XPATH, '//input[@data-test="username"]')
    password_input_loc = (By.XPATH, '//input[@data-test="password"]')
    login_button_loc = (By.ID, 'login-button')

    red_cross = (By.XPATH, '//*[@data-prefix="fas"]')