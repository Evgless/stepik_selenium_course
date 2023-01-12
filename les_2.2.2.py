import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)     # скролл для видимости объекта
    #browser.execute_script("window.scrollBy(0, 100);")      # скролл на 100 пикселей вниз
    #button.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    result = browser.find_element(By.CSS_SELECTOR, "#answer")
    result.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    #time.sleep(2)
    browser.execute_script("window.scrollBy(0, 100);")
    #time.sleep(2)
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(2)

finally:
    time.sleep(5)
    browser.quit()