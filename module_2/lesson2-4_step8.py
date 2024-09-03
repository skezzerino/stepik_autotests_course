from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

book = WebDriverWait(browser, 13).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
browser.find_element(By.ID, 'book').click()

x = browser.find_element(By.ID, 'input_value').text
browser.find_element(By.ID, 'answer').send_keys(calc(x))

browser.find_element(By.ID, 'solve').click()

time.sleep(3)

browser.quit()
