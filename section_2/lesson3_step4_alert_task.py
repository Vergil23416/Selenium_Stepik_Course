from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button_alert = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_alert.click()

    alert_notification = browser.switch_to.alert
    alert_notification.accept()
    # Небольшая задержка перед работой с новой страницей
    time.sleep(1)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(x_element)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
