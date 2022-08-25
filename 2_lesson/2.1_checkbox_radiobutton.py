from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/math.html'
try:
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x =x_element.text
    y = calc(x)
    x_input = browser.find_element(By.ID, 'answer')
    x_input.send_keys(y)
    
    checkbox = browser.find_element(By.CSS_SELECTOR, 'label[for = "robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value = "robots"]')
    radiobutton.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    button_submit.click()
finally:
    time.sleep(30)
    browser.close()