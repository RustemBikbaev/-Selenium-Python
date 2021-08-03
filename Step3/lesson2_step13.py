from selenium import webdriver
import time
import unittest 

class Test_Registation(unittest.TestCase):
	def test_reg_first(self):		 
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
		input1.send_keys("1111")
		input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
		input2.send_keys("2222")
		input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
		input3.send_keys("3333")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		expected_rethalt = "Congratulations! You have successfully registered!"
		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(expected_rethalt , welcome_text , f"First test FAILD:/n Expected {expected_rethalt}, but was {welcome_text}")

		# ожидание чтобы визуально оценить результаты прохождения скрипта
		time.sleep(3)
		# закрываем браузер после всех манипуляций
		browser.quit()
		
		
	def test_reg_second(self):		 
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
		input1.send_keys("1111")
		input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
		input2.send_keys("2222")
		input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
		input3.send_keys("3333")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		expected_rethalt = "Congratulations! You have successfully registered!"
		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(expected_rethalt , welcome_text , f"Second test FAILD:/n Expected {expected_rethalt}, but was {welcome_text}")

		# ожидание чтобы визуально оценить результаты прохождения скрипта
		time.sleep(3)
		# закрываем браузер после всех манипуляций
		browser.quit()		

if __name__ == "__main__":
    unittest.main()		