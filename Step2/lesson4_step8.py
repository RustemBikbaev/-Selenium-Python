from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:	
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h5#price"),"$100"))
	
	button = browser.find_element_by_css_selector("button#book")
	button.click()
	
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
	
