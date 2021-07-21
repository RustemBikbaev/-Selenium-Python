from selenium import webdriver
import time
import math

try:    
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    people_radio = browser.find_element_by_id("peopleRule")
    
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"
    
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None
    
    button = browser.find_element_by_css_selector("button.btn-default[type='submit']")
    buttons_disabled = button.get_attribute("disabled")
    print("button disabled: ", buttons_disabled)
    time.sleep(20)
    
    button = browser.find_element_by_css_selector("button.btn-default[type='submit']")
    buttons_disabled = button.get_attribute("disabled")    
    print("button disabled: ", buttons_disabled)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
