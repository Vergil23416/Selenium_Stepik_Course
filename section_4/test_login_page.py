from pages.login_page import LoginPage
from selenium import webdriver
import pytest, time, math


def test_guest_should_be_login_and_register_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
