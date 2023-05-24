from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    msg = browser.find_element(By.ID, "verify_message")

    assert "successful" in msg.text

finally:
    browser.quit()
