from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:    
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x1 = int(browser.find_element_by_css_selector(".nowrap#num1").text)
    x2 = int(browser.find_element_by_css_selector(".nowrap#num2").text)    
    
    
    select = Select(browser.find_element_by_css_selector("select#dropdown.custom-select"))
    select.select_by_value(str(x1+x2)) # ищем элемент с текстом "Python".click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
