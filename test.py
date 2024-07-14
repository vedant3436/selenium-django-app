from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class LoginFormTest(LiveServerTestCase):

	def testform(self):
		
		fService = webdriver.FirefoxService(executable_path=r'PATH_TO_geckodriver.exe')
		driver = webdriver.Firefox(service= fService)

		driver.get('WEBSITE_URL')

		time.sleep(3)

		full_name = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i1']")
		contact_number = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i5']")
		email_id = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i9']")
		full_address = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i13']")
		pincode = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i17']")
		dob_month = driver.find_element(By.CSS_SELECTOR,"[aria-label='Month']")
		dob_day = driver.find_element(By.CSS_SELECTOR,"[aria-label='Day of the month']")
		dob_year = driver.find_element(By.CSS_SELECTOR,"[aria-label='Year']")
		gender = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i25']")
		verify_code = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='i29']")

		time.sleep(3)

		#submit = driver.find_element(By.CLASS_NAME,'l4V7wb Fxmcue')
		
		full_name.send_keys('xxxx')
		contact_number.send_keys('xxxx')
		email_id.send_keys('xxxx')
		full_address.send_keys('xxxx')
		pincode.send_keys('xxxx')
		dob_month.send_keys('xxxx')
		dob_day.send_keys('xxxx')
		dob_year.send_keys('xxxx')
		gender.send_keys('xxxx')
		verify_code.send_keys('xxxx')

		driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
		driver.save_screenshot(r"PATH_TO_SAVE_SCREENSHOT")
