from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    input_value_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='input_value']"))
    )
    input_value = input_value_element.text
    result_value = calc(input_value)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result_value)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()
