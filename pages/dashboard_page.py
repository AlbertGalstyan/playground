from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Dashboard(BasePage):
    header_element = (By.TAG_NAME, "h1")

    # def __init__(self, driver):
    #     self.driver = driver

    def get_header_element(self):
        header = self.driver.find_element(*self.header_element)
        return header.text
