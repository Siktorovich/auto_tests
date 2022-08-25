import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    url = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()

    browser.get(url)
    current_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '2.2_downloading_files.py')
    browser.find_element(By.CSS_SELECTOR,"input[name='firstname']").send_keys('Anton')
    browser.find_element(By.CSS_SELECTOR,"input[name='lastname']").send_keys('Momot')
    browser.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys('test@.ru')
    browser.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(current_file)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    button.click()


finally:
    time.sleep(30)
    browser.close()