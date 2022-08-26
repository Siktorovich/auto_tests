import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestSelectors(unittest.TestCase):


    def test_new_link(self):
        link_old = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link_old)

        input1 = browser.find_element(By.CSS_SELECTOR,
        'div.first_class > input.first[placeholder = "Input your first name"]')
        input1.send_keys('Anton')
        input2 = browser.find_element(By.CSS_SELECTOR,
        'div.second_class > input.second[placeholder = "Input your last name"]')
        input2.send_keys('Momot')
        input3 = browser.find_element(By.CSS_SELECTOR,
        'div.third_class > input.third[placeholder = "Input your email"]')
        input3.send_keys('test@mail.ru')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'There is not "welcome_text on page')

    def test_old_link(self):
        link_new = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link_new)

        input1 = browser.find_element(By.CSS_SELECTOR,
        'div.first_class > input.first[placeholder = "Input your first name"]')
        input1.send_keys('Anton')
        input2 = browser.find_element(By.CSS_SELECTOR,
        'div.second_class > input.second[placeholder = "Input your last name"]')
        input2.send_keys('Momot')
        input3 = browser.find_element(By.CSS_SELECTOR,
        'div.third_class > input.third[placeholder = "Input your email"]')
        input3.send_keys('test@mail.ru')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'There is not "welcome_text on page')


if __name__ == '__main__':
    unittest.main()
