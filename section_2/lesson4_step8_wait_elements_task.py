from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # Задает время ожидания перед появлением элемента на странице и работой с ним
    # browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # Ожидаем 12 секунд, если цена становится $100, то кликаем, иначе ошибка
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(x_element)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(result)

    button_solve = browser.find_element(By.CSS_SELECTOR, "#solve")
    button_solve.click()

finally:
    time.sleep(5)
    browser.quit()
