import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value').text


    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # time.sleep(3)

    print(browser.switch_to.alert.text)
finally:
    browser.quit()
