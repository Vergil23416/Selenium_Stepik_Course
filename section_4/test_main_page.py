from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from selenium import webdriver
import pytest, time, math


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, url=browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_received_notification_basket_is_empty()
