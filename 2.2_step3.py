from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(executable_path="C:\\Users\\user\\Documents\\pyauto\\chromedriver.exe")
    browser.get(link)
    def calc(x, y):
        return str(int(x) + int(y))
    num1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']").text
    num2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']").text
    x, y = num1, num2
    number = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(number)

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(5)
    browser.quit()