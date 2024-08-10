from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Hooks to manage the browser
def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()

@given('I am on the Demo Login Page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account "{user_type}"')
def step_impl(context, user_type):
    credentials = {
        "standard_user": ("standard_user", "secret_sauce"),
        "locked_out_user": ("locked_out_user", "secret_sauce")
    }
    username, password = credentials[user_type]
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the Login Button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I am redirected to the Demo Main Page')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url

@then('I verify the App Logo exists')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "app_logo").is_displayed()

@then('I verify the Error Message contains the text "{message}"')
def step_impl(context, message):
    error_message = context.driver.find_element(By.CLASS_NAME, "error-message-container error").text
    assert message in error_message

@given('I am on the inventory page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when('user sorts products from high price to low price')
def step_impl(context):
    sort_dropdown = Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("hilo")

@when('user adds highest priced product')
def step_impl(context):
    context.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()

@when('user clicks on cart')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

@when('user clicks on checkout')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()

@when('user enters first name "{first_name}"')
def step_impl(context, first_name):
    context.driver.find_element(By.ID, "first-name").send_keys(first_name)

@when('user enters last name "{last_name}"')
def step_impl(context, last_name):
    context.driver.find_element(By.ID, "last-name").send_keys(last_name)

@when('user enters zip code "{zip_code}"')
def step_impl(context, zip_code):
    context.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

@when('user clicks Continue button')
def step_impl(context):
    context.driver.find_element(By.ID, "continue").click()

@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_impl(context):
    total = context.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert "$49.99" in total

@when('user clicks Finish button')
def step_impl(context):
    context.driver.find_element(By.ID, "finish").click()

@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert header == "THANK YOU FOR YOUR ORDER"
