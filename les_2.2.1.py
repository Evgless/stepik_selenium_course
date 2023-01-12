import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #select = Select(browser.find_element(By.TAG_NAME, "select"))

    #browser.find_element(By.TAG_NAME, "select").click()    # раскрытие списка
    #time.sleep(2)
    #browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()   # выбор второго элемента списка
    #browser.find_element(By.CSS_SELECTOR, "[value='1']").click()   # выбор элемента со значением 1
    #select.select_by_value("1") # выбор элемента списка без раскрытия списка

    num_1 = browser.find_element(By.ID, "num1")
    x = int(num_1.text)     # выбор видимого текста
    #print(x)
    num_2 = browser.find_element(By.ID, "num2")
    y = int(num_2.text)     # выбор видимого текста
    #print(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x + y))

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(5)
    browser.quit()