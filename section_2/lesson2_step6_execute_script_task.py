from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group #input_value")
    x_element = x_element.text
    answer = calc(x_element)

    input_answer = browser.find_element(By.CSS_SELECTOR, "div.form-group #answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(answer)

    robot_check_box = browser.find_element(
        By.CSS_SELECTOR, "div.form-check [for='robotCheckbox']"
    )
    robot_check_box.click()

    robot_radio_button = browser.find_element(
        By.CSS_SELECTOR, "div.form-check [for='robotsRule']"
    )
    robot_radio_button.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
