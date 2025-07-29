from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest, time, math


def calc():
    return math.log(int(time.time()))


@pytest.mark.authorization
@pytest.mark.parametrize(
    "page_url",
    ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"],
)
class TestLoginStepik:

    def test_links_stepik(self, authorize_stepik, wait, page_url):
        browser_now = authorize_stepik
        link = f"https://stepik.org/lesson/{page_url}/step/1"
        expected_text = "Correct!"
        browser_now.get(link)

        textarea_input = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "textarea.ember-text-area")
            )
        )
        textarea_input.send_keys(calc())

        button_submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button_submit.click()

        actual_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        ).text
        assert expected_text == actual_text
