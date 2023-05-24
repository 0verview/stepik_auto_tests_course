import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    browser.switch_to.window(browser.window_handles[1])
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    result_value = calc(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result_value)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()