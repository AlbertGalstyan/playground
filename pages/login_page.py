from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Login(BasePage):
    email_field = (By.ID, "email-field")
    password_field = (By.ID, "password-field")
    login_btn = (By.ID, "submitBtn")

    # def __init__(self, driver):
    #     self.driver = driver

    def enter_username(self):
        self.driver.find_element(*self.email_field).send_keys("testingart@email.com")

    def enter_password(self):
        self.driver.find_element(*self.password_field).send_keys("Testing!123")

    def login_btn_click(self):
        self.driver.find_element(*self.login_btn).click()
