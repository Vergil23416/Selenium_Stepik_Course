from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_links(link):

    try:
        browser= webdriver.Chrome()
        browser.get(link)

        num1=browser.find_element(By.ID,"num1").text
        num2=browser.find_element(By.ID,"num2").text
        sum_nums=int(num1)+int(num2)

        select=Select(browser.find_element(By.ID,"dropdown"))
        select.select_by_value(str(sum_nums))

        button=browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()

test_links("http://suninjuly.github.io/selects1.html")
test_links("http://suninjuly.github.io/selects2.html")