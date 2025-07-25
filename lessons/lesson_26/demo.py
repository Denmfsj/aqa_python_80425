from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://127.0.0.1:8000/lessons/lesson_26/html_docs/demo.html")

# Знаходження всіх елементів з тегом <li>
li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break

driver.quit()