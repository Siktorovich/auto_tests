from selenium import webdriver


try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get("https://stepik.org/lesson/25969/step/8")
finally:
    driver.close()
