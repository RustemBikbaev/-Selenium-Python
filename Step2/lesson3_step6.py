from selenium import webdriver
import time
import math

try:    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
	
    x = int(browser.find_element_by_css_selector("span#input_value").text)    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input2 = browser.find_element_by_css_selector("input[id='answer']")
    input2.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn-primary[type='submit']")
    button.click()
    
finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
