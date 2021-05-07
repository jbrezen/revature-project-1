from selenium.webdriver.chrome.webdriver import WebDriver


class LogInPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def user_box(self):
        return self.driver.find_element_by_id("username")

    def pass_box(self):
        return self.driver.find_element_by_id("password")

    def submit_button(self):
        return self.driver.find_element_by_id("submit")