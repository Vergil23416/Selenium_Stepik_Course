from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest, json, os


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    # Получаем язык браузера
    parser.addoption(
        "--language",
        action="store",
        default="fr",  # Язык по умолчанию
        help="Choose language for the browser (e.g., es, fr, ru, en)",
    )


# Фикстура браузера
@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# Ожидание для браузера
@pytest.fixture(scope="class")
def wait(browser):
    return WebDriverWait(browser, 10)


# Получаем логин и пароль от степика
@pytest.fixture(scope="session")
def load_login_and_password():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(current_dir, "config.json")
    try:
        with open(config_path, "r") as file:
            config_user_data = json.load(file)
            return config_user_data
    except:
        pytest.fail(f"Файл не найден")


@pytest.fixture(scope="class")
def authorize_stepik(browser, wait, load_login_and_password):
    link = "https://stepik.org/lesson/236895/step/1"
    user_data = load_login_and_password
    browser.get(link)

    button_login = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember479"))
    )
    button_login.click()
    # Ожидаем появление окна логина
    login_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
    )
    login_input.send_keys(user_data["email"])
    password_input = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password_input.send_keys(user_data["password"])

    button_send = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button_send.click()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img.navbar__profile-img"))
    )
    yield browser
