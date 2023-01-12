import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    find_link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    time.sleep(2)

    find_link.click()
    time.sleep

    find_form_fname = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    find_form_fname.send_keys("First")
    find_form_lname = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    find_form_lname.send_keys("Last")
    find_form_city = browser.find_element(By.CLASS_NAME, "city")
    find_form_city.send_keys("City")
    find_form_country = browser.find_element(By.ID, "country")
    find_form_country.send_keys("Country")

    submit = browser.find_element(By.CLASS_NAME, "btn-default")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
