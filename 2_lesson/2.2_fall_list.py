from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    url = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(url)
    sum = int(browser.find_element(By.CSS_SELECTOR, 'span#num1').text) + int(browser.find_element(By.CSS_SELECTOR, 'span#num2').text)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(sum))

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.close()