from selenium import webdriver
import time
import os

try:    
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    input_FN = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    input_FN.send_keys("123")
    
    input_LN = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    input_LN.send_keys("123")
    
    input_Mail = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    input_Mail.send_keys("123")
	
    input_file = browser.find_element_by_css_selector("input[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt') 
    input_file.send_keys(file_path)

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
    
    
