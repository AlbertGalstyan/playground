import pytest

from pages.dashboard_page import Dashboard
from pages.login_page import Login


def test_valid_login(driver):
    login_page = Login(driver)
    assert driver.title == "Playground"
    login_page.enter_username()
    login_page.enter_password()
    login_page.login_btn_click()

# Comment

