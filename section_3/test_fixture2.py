import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# function, class, module, session - для каждой функции, класса, модуля, сессии
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    # Выход из браузера произойдет после окончания теста
    print("\nquit browser..")
    browser.quit()


# Запускаем фикстуру для каждого теста, даже если она не указана
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
