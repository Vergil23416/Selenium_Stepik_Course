from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


# Параметризация - позволяет использовать разные значения для тестов
# @pytest.mark.parametrize("language",["ru","en-gb"]) - параметризация для всего класса, все методы два раза выполнятся
class TestLogin:
    @pytest.mark.parametrize("language", ["ru", "en-gb"])
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
