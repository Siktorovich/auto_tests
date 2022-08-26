import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math




class TestLinkUFO():

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_link(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(20)
        answer = math.log(int(time.time()))
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)

        # button = WebDriverWait(browser, 12).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission[type="button"]'))
        # )
        button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission[type="button"]')
        button.click()

        # correct = WebDriverWait(browser, 12).until(
        #     EC.visibility_of((By.CSS_SELECTOR, 'div > p.smart-hints__hint'))
        # )
        correct = browser.find_element(By.CSS_SELECTOR, 'div > p.smart-hints__hint')

        assert correct.text == 'Correct!', f'Not correct {link}'
