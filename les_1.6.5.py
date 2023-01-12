import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_form_fname = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    find_form_fname.send_keys("First")
    find_form_lname = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    find_form_lname.send_keys("Last")
    find_form_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    find_form_email.send_keys("Email")
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()