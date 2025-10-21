# Test script
from selenium import webdriver
from libs.ui_libs.create_account_libs import CreateAccountLibs

def test_create_account():
    driver = webdriver.Chrome()
    driver.maximize_window()
    create_lib = CreateAccountLibs(driver)

    try:
        create_lib.create_account_test()
    finally:
        driver.quit()
