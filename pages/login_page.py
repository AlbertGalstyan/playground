from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email-field")
        self.password_field = (By.ID, "password-field")
        self.login_btn = (By.ID, "submitBtn")

    def enter_username(self):
        self.driver.find_element(*self.email_field).send_keys("testingart@email.com")

    def enter_password(self):
        self.driver.find_element(*self.password_field).send_keys("Testing!123")

    def login_btn_click(self):
        self.driver.find_element(*self.login_btn).click()
