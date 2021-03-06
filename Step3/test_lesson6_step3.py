import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

@pytest.fixture(scope="function")
def browser():
	options = webdriver.ChromeOptions()
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	browser = webdriver.Chrome(options=options)
	yield browser
	browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestMainPage1():

	def test_open_link(self, browser, link):		
		browser.get(link)
		browser.implicitly_wait(5)
		input = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
		answer = math.log(int(time.time()))
		input.send_keys(str(answer))
		button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
		button.click()
		output = browser.find_element_by_css_selector("pre.smart-hints__hint")
		if output.text != "Correct!":
			print("\n ============"+output.text+"============\n")
			assert output.text == "Correct!", "Output is not 'Correct!'"

