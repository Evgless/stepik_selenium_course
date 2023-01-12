import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]      # узнаем имя новой вкладки
    browser.switch_to.window(new_window)        # переключаемся на вкладку по имени

    #confirm = browser.switch_to.alert
    #confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()