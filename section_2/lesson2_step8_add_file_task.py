from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
import os, time

faker = Faker("ru_RU")

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_first_name.send_keys(faker.first_name())

    input_last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_last_name.send_keys(faker.last_name())

    input_email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_email.send_keys(faker.email())

    input_file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file_l2_step8.txt")
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
