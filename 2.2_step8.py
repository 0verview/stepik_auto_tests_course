import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.NAME, 'firstname').send_keys("First Name")
    browser.find_element(By.NAME, 'lastname').send_keys("Last Name")
    browser.find_element(By.NAME, 'email').send_keys("email@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.XPATH, "//input[@id='file']").send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(10)
    browser.quit()
