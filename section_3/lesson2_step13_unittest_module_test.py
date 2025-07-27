from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time, unittest, pytest


fake = Faker("ru_RU")


def generate_user_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.street_address(),
    }


class TestAssert(unittest.TestCase):
    # Открытие экземпляра браузера и создание юзера для каждого теста (self), выполняется до каждого теста
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = generate_user_data()

    # Выполняется после теста
    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    # Основная логика работы на странице
    def main_logic_links(self, link):
        self.browser.get(link)

        input_first_name = self.browser.find_element(
            By.CSS_SELECTOR, "div.first_block input.form-control.first"
        )
        input_first_name.send_keys(self.user["first_name"])

        input_last_name = self.browser.find_element(
            By.CSS_SELECTOR, "div.first_block input.form-control.second"
        )
        input_last_name.send_keys(self.user["last_name"])

        input_email = self.browser.find_element(
            By.CSS_SELECTOR, "div.first_block input.form-control.third"
        )
        input_email.send_keys(self.user["email"])

        input_phone = self.browser.find_element(
            By.CSS_SELECTOR, "div.second_block input.form-control.first"
        )
        input_phone.send_keys(self.user["phone"])

        input_address = self.browser.find_element(
            By.CSS_SELECTOR, "div.second_block input.form-control.second"
        )
        input_address.send_keys(self.user["address"])

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Пауза для ожидания регистрации
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # возвращаем результат теста
        return welcome_text

    # Положительный тест-кейс
    def test_link_success(self):
        expected_text = "Congratulations! You have successfully registered!"
        actual_text = self.main_logic_links(
            "http://suninjuly.github.io/registration1.html"
        )
        self.assertEqual(expected_text, actual_text, "Ожидаемый текст не совпадает")

    # Негативный тест-кейс (Отсутствие важного элемента на странице)
    def test_link_failure(self):
        expected_text = "Congratulations! You have successfully registered!"
        actual_text = self.main_logic_links(
            "http://suninjuly.github.io/registration2.html"
        )
        self.assertEqual(expected_text, actual_text, "Ожидаемый текст не совпадает")


if __name__ == "__main__":
    unittest.main()
