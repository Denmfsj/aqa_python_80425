from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ініціалізуємо драйвер Chrome
driver = webdriver.Chrome()

# Відкриваємо головну сторінку
driver.get("http://127.0.0.1:8000/lessons/lesson_26/html_docs/scrool_frame.html")

# Прокрутка вниз
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)  # Зачекайте трохи після прокрутки вниз

# Прокрутка вгору
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)  # Зачекайте трохи після прокрутки вгору

# Перемикаємося до фрейму
driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))

# Натискання на кнопку три рази
for _ in range(3):
    button = driver.find_element(By.ID, "myButton")
    button.click()
    time.sleep(1)  # Зачекайте трохи після кожного натискання



driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.switch_to.default_content()  # переключення до дефолтнго фрейму
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

h1_el = driver.find_element(By.XPATH, '//h1')
h1_loc = tuple(h1_el.location.values())
driver.execute_script(f"window.scrollTo{h1_loc};")  # скор до елемента '//h1' по координатам
# Закриваємо браузер
driver.quit()