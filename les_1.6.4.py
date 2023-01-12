import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    text_fname = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    text_fname.send_keys("First")
    text_lname = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    text_lname.send_keys("Last")
    text_city = browser.find_element(By.CLASS_NAME, "city")
    text_city.send_keys("City")
    text_country = browser.find_element(By.ID, "country")
    text_country.send_keys("Country")

    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
