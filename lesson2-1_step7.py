from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# можно поместить функцию до try, а можно и внутри try
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer").send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox").click()

    robots = browser.find_element(By.ID, "robotsRule").click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(2)
    browser.quit()
