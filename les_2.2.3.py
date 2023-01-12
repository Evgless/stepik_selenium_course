import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_form_fname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    find_form_fname.send_keys("First")
    find_form_lname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    find_form_lname.send_keys("Last")
    find_form_city = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    find_form_city.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_name = "file1.txt"
    file_path = os.path.join(current_dir, 'file1.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()