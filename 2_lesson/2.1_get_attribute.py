from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    img_x = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    value_x = img_x.get_attribute('valuex')
    y = calc(value_x)

    input_space = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_space.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
    radiobutton.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    button_submit.click()

finally:
    time.sleep(30)
    browser.close()