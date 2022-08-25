from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#
# url = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(url)
#
#     arr = browser.find_elements(By.TAG_NAME, 'input')
#     for i in range(len(arr)):
#         arr[i].send_keys('Empty')
#     button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()
# #############################################################################
# url = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(url)
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys('Anton')
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys('Momot')
#     input3 = browser.find_element(By.CLASS_NAME, 'city')
#     input3.send_keys('Moscow')
#     input4 = browser.find_element(By.ID, 'country')
#     input4.send_keys('Russia')
#     button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

try:
    # link_old = "http://suninjuly.github.io/registration1.html"
    link_new = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link_new)

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_class > input.first[placeholder = "Input your first name"]')
    input1.send_keys('Anton')
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.second_class > input.second[placeholder = "Input your last name"]')
    input2.send_keys('Momot')
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.third_class > input.third[placeholder = "Input your email"]')
    input3.send_keys('test@mail.ru')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
