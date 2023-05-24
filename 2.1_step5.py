import math
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    try:
        link = "https://suninjuly.github.io/math.html   "
        browser = webdriver.Chrome(executable_path="C:\\Users\\user\\Documents\\pyauto\\chromedriver.exe")
        browser.get(link)
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
        input1.send_keys(y)
        input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
        input2.click()
        input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
        input3.click()
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()

    finally:
        time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()