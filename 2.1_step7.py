import math
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    try:
        link = "http://suninjuly.github.io/get_attribute.html"
        browser = webdriver.Chrome(executable_path="C:\\Users\\user\\Documents\\pyauto\\chromedriver.exe")
        browser.get(link)

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
        x = x_element
        y = calc(x)

        input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
        input1.send_keys(y)
        input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        input2.click()
        input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
        input3.click()
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()

    finally:
        time.sleep(1)

finally:
    time.sleep(3)
    browser.quit()