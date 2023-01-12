import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    result = browser.find_element(By.CSS_SELECTOR, "#answer")
    result.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()