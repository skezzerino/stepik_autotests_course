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

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option2.click()

    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitbutton.click()

finally:
    time.sleep(3)
    browser.quit()
