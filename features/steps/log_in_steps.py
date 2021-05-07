from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.log_in import LogInPage


@given('The user is on the log in page')
def get_to_log_in(context):
    driver: WebDriver = context.driver
    driver.get("http://127.0.0.1:8000/login.html/")


@when('The user inputs correct {usr} and {pw}')
def log_in_correct(context, usr, pw):
    log_in_page: LogInPage = context.log_in_page
    log_in_page.user_box().send_keys(usr)
    log_in_page.pass_box().send_keys(pw)


@when('The user inputs incorrect {usr} and {pw}')
def log_in_correct(context, usr, pw):
    log_in_page: LogInPage = context.log_in_page
    log_in_page.user_box().send_keys(usr)
    log_in_page.pass_box().send_keys(pw)


@when('The user clicks Submit')
def submit_credentials(context):
    log_in_page: LogInPage = context.log_in_page
    log_in_page.submit_button().click()


@then('The user is taken to the form submission page')
def verify_submission(context):
    driver: WebDriver = context.driver
    assert driver.title == "Reimbursement - Submit Request"


@then('The user is not taken to the form submission page')
def verify_failure(context):
    driver: WebDriver = context.driver
    assert driver.title != "Reimbursement - Submit Request"


