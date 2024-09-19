from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.header_element = (By.TAG_NAME, "h1")

    def get_header_element(self):
        header = self.driver.find_element(*self.header_element)
        return header.text
