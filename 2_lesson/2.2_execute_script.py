from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()

    browser.get(url)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    inp = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
    inp.send_keys(y)


    browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]').click()

    button.click()


finally:
    time.sleep(30)
    browser.close()
