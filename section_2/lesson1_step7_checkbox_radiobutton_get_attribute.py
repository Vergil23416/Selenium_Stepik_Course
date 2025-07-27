from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element=browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_element=x_element.get_attribute("valuex")
    answer=calc(x_element)

    input_answer=browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(answer)

    robot_check_box=browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    robot_check_box.click()

    robot_radio_button=browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    robot_radio_button.click()

    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()


