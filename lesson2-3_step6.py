import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.CLASS_NAME, 'trollface').click()

    first_window = browser.window_handles[0] # запоминаем текущую вкладку
    new_window = browser.window_handles[1] # запоминаем новую вкладку
    browser.switch_to.window(new_window) # переводим драйвер на новую вкладку

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(3)

    # print(browser.switch_to.alert.text)
finally:
    browser.quit()
