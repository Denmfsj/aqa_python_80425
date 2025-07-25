from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/lessons/lesson_26/html_docs/dialogs.html")

# Показати Alert і отримати текст з нього
driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
alert = Alert(driver)
print("Текст Alert:", alert.text)
alert.accept()

# Показати Confirm і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
alert = Alert(driver)
print("Текст Confirm:", alert.text)
alert.accept()

# Показати Prompt, ввести текст і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
alert = Alert(driver)
print("Текст Prompt:", alert.text)
alert.send_keys("John")
alert.accept()

# Зачекати 2 секунди перед завершенням
time.sleep(2)

# Закрити браузер
driver.quit()