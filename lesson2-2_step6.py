from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# time.sleep(3)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) # делаем скролл до видимости элемента в верхней части страницы, без него элемент закрыт футтером
# browser.execute_script("window.scrollBy(0, 100);") # делаем скролл на количество заданных пикселей. Первое значение - влево/вправо, второе - вниз/вверх
# time.sleep(3)
# button.click()

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    xfunc = math.log(abs(12*math.sin(x)))
    answer = browser.find_element(By.ID, "answer").send_keys(xfunc)

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(3)
finally:
    browser.quit()
