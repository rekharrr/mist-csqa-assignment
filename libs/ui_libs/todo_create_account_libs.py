from utils.ui_utils.ui_utils import UIUtils
from selenium import webdriver

class CreateAccountLibs:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ui_utils = UIUtils(driver)

    def navigate_to_create_account_page(self):
        """Navigate to the create account page"""
        self.ui_utils.navigate_to("https://manage.ac2.mist.com/signin.html#!signup/register")

    # TODO - Candidate to add libs for Create Account functionalities when working on the assignment.