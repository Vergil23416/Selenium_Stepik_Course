from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Basket is not empty"

    def should_be_received_notification_basket_is_empty(self):
        basket_text = self.browser.find_element(
            *BasketPageLocators.MESSAGE_BASKET_IS_EMPTY
        ).text
        assert "Ваша корзина пуста" in basket_text, "Not notification"
