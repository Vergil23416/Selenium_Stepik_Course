from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time


fake = Faker("ru_RU")


def generate_user_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.street_address(),
    }


new_user = generate_user_data()

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block input.form-control.first"
    )
    input_first_name.send_keys(new_user["first_name"])

    input_last_name = browser.find_element(
        By.CSS_SELECTOR, "div.first_block input.form-control.second"
    )
    input_last_name.send_keys(new_user["last_name"])

    input_email = browser.find_element(
        By.CSS_SELECTOR, "div.first_block input.form-control.third"
    )
    input_email.send_keys(new_user["email"])

    input_phone = browser.find_element(
        By.CSS_SELECTOR, "div.second_block input.form-control.first"
    )
    input_phone.send_keys(new_user["phone"])

    input_address = browser.find_element(
        By.CSS_SELECTOR, "div.second_block input.form-control.second"
    )
    input_address.send_keys(new_user["address"])

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Пауза для ожидания регистрации
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
