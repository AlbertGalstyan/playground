import pytest

from pages.dashboard_page import Dashboard
from pages.login_page import Login


def test_e2e(driver):
    login_page = Login(driver)
    assert driver.title == "Playground"
    login_page.enter_username()
    login_page.enter_password()
    login_page.login_btn_click()

    dashboard_page = Dashboard(driver)
    assert dashboard_page.get_header_element() == "Welcome to Automation Testing Playground"

# Comment

