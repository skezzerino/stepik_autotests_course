import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.NAME, 'firstname').send_keys('abs')

last_name = browser.find_element(By.NAME, 'lastname').send_keys('sba')

email = browser.find_element(By.NAME, 'email').send_keys('abs.sba@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(3)
