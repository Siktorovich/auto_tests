from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, 'form > div > div > button[type="submit"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(0.5)

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]').click()


finally:
    time.sleep(30)
    browser.close()