from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")
browser.find_element(By.ID, "button")
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text
browser.quit()
