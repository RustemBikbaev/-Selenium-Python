from selenium import webdriver
import time
import math

try:    
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 150);")
    # Ваш код, который заполняет обязательные поля
    x = int(browser.find_element_by_css_selector("span#input_value").text)    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input2 = browser.find_element_by_css_selector("input[id='answer']")
    input2.send_keys(y)
    
    input_checkbox = browser.find_element_by_css_selector("input.form-check-input[id='robotCheckbox']")
    input_checkbox.click()
    
    input_radiobuttons = browser.find_element_by_css_selector("input.form-check-input[id='robotsRule']")
    input_radiobuttons.click()

    # Отправляем заполненную форму
    
    #browser.execute_script("window.scrollBy(0, 150);")
    #time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn-primary[type='submit']")
    button.click()


finally:


 
	
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
