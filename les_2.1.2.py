import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    chest = browser.find_element(By.ID, "treasure")
    x = chest.get_attribute("valuex")
    y = calc(x)
    result = browser.find_element(By.ID, "answer")
    result.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()