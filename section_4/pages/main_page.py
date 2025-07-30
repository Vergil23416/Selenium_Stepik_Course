from .base_page import BasePage
from .locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
import pytest, time, math


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
