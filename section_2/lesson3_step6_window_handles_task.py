from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button_magic = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button_magic.click()
    # Запоминаем наименование второй вкладки
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(x_element)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
