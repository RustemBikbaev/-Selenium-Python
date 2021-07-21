from selenium import webdriver
import time
import math

try:    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = int(browser.find_element_by_css_selector("img[src='images/chest.png']").get_attribute("valuex"))    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input2 = browser.find_element_by_css_selector("input[id='answer']")
    input2.send_keys(y)
    
    input_checkbox = browser.find_element_by_css_selector("input.check-input[id='robotCheckbox']")
    input_checkbox.click()
    
    input_radiobuttons = browser.find_element_by_css_selector("input.check-input[id='robotsRule']")
    input_radiobuttons.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
