from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


import time


def test_add_to_cart_button_availability(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_elements(
        By.CSS_SELECTOR, ".btn-add-to-basket"), "button is missing"
