import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_profile = Options()      # создаем переменную с настройками браузера
FILE_NAME_PROFILE = "C:\\Users\\Johnny\\AppData\\Local\\Google\\Chrome\\User Data"      # сохраняем путь к профилям хрома в переменную
chrome_profile.add_argument("user-data-dir=" + FILE_NAME_PROFILE)       # в переменную с настройками прописываем путь к профилям
browser = webdriver.Chrome(options=chrome_profile)      # запускаем окно хрома с настройками

link = "https://vk.com"
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "#l_msg span.left_label.inl_bl").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '[data-list-id="51412233"]').click()
    time.sleep(1)
    msg = browser.find_element(By.CSS_SELECTOR, ".im_editable.im-chat-input--text._im_text")
    msg.send_keys('Привет, Иван', Keys.RETURN)
    time.sleep(1)
    msg.send_keys('Пойдешь играть?', Keys.RETURN)
    time.sleep(1)
    msg.send_keys('Get The Fuck Out', Keys.RETURN)
    time.sleep(1)
    msg.send_keys('Гы, сообщения отправлены с помощью Selenium', Keys.RETURN)
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()