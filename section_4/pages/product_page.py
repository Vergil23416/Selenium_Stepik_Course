from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
        )
        button_add_to_basket.click()

    def should_be_success_message_with_product_name(self):
        actual_product_name = self.browser.find_element(
            By.CSS_SELECTOR, "div.alertinner strong"
        ).text
        extended_product_name = self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT
        ).text
        assert actual_product_name == extended_product_name, "Не тот продукт"

    def should_be_message_basket_price_equal_price_product(self):
        actual_price = self.browser.find_element(
            By.CSS_SELECTOR, "div.alertinner > p strong"
        ).text
        extended_price = self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT
        ).text
        assert actual_price == extended_price, "Цена не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            By.CSS_SELECTOR, "div.alertinner strong"
        ), "Подтверждающее сообщение появилось"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            By.CSS_SELECTOR, "div.alertinner strong"
        ), "Подтверждающее сообщение не пропало"
