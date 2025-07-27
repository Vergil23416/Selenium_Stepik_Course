from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_element=browser.find_element(By.CSS_SELECTOR, "div.form-group #input_value")
    x_element=x_element.text
    answer=calc(x_element)

    input_answer=browser.find_element(By.CSS_SELECTOR, "div.form-group #answer")
    input_answer.send_keys(answer)

    robot_check_box=browser.find_element(By.CSS_SELECTOR,"div.form-check [for='robotCheckbox']")
    robot_check_box.click()

    robot_radio_button=browser.find_element(By.CSS_SELECTOR,"div.form-check [for='robotsRule']")
    robot_radio_button.click()

    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
