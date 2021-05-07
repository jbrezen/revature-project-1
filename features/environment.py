from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.log_in import LogInPage


def before_all(context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome('C:/Users/jerem/Documents/chromedriver.exe', chrome_options=options)

    log_in_page = LogInPage(driver)

    context.driver = driver
    context.log_in_page = log_in_page


def after_all(context):
    context.driver.quit()
