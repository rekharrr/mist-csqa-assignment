from utils.ui_utils.ui_utils import UIUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class CreateAccountLibs:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ui_utils = UIUtils(driver)

    def navigate_to_create_account_page(self):
        """Navigate to the create account page"""
        self.ui_utils.navigate_to("https://manage.ac2.mist.com/signin.html#!signup/register")

    def fill_first_name(self, first_name="Test"):
        """Fill the first name field"""
        self.ui_utils.send_keys(By.NAME, "firstName", first_name)
        print(f"Filled first name: {first_name}")

    def fill_last_name(self, last_name="User"):
        """Fill the last name field"""
        self.ui_utils.send_keys(By.NAME, "lastName", last_name)
        print(f"Filled last name: {last_name}")

    def fill_email(self, email="testuser@example.com"):
        """Fill the email field"""
        self.ui_utils.send_keys(By.NAME, "email", email)
        print(f"Filled email: {email}")

    def fill_password(self, password="TestPassword123!"):
        """Fill the password field"""
        self.ui_utils.send_keys(By.NAME, "password", password)
        print("Filled password")

    def fill_company_name(self, company_name="Test Company"):
        """Fill the company name field"""
        self.ui_utils.send_keys(By.NAME, "companyName", company_name)
        print(f"Filled company name: {company_name}")

    def fill_company_address1(self, address="123 Test Street"):
        """Fill the company address 1 field and select first suggestion"""
        self.ui_utils.send_keys(By.NAME, "data-input-field", address)
        print(f"Filled company address 1: {address}")
        time.sleep(2)  # Wait for suggestions to appear
        # Click the first suggestion
        suggestions = self.driver.find_elements(By.CSS_SELECTOR, ".suggestion-item, .autocomplete-item, [role='option']")
        if suggestions:
            suggestions[0].click()
            print("Selected first address suggestion")

    def fill_company_address2(self, address="Suite 100"):
        """Fill the company address 2 field"""
        self.ui_utils.send_keys(By.NAME, "companyAddress2", address)
        print(f"Filled company address 2: {address}")

    def fill_city(self, city="San Francisco"):
        """Fill the city field"""
        self.ui_utils.send_keys(By.NAME, "city", city)
        print(f"Filled city: {city}")

    def fill_zip_code(self, zip_code="94105"):
        """Fill the zip code field"""
        self.ui_utils.send_keys(By.NAME, "zipCode", zip_code)
        print(f"Filled zip code: {zip_code}")

    def select_state(self):
        """Select state from dropdown"""
        selects = self.driver.find_elements(By.TAG_NAME, "select")
        if len(selects) >= 1:
            select = Select(selects[0])
            # Select the first available option (skip placeholder)
            if len(select.options) > 1:
                select.select_by_index(1)
                print("Selected state")
            else:
                print("No state options to select")

    def select_country(self):
        """Select country from dropdown"""
        selects = self.driver.find_elements(By.TAG_NAME, "select")
        if len(selects) >= 2:
            select = Select(selects[1])
            # Select the first available option (skip placeholder)
            if len(select.options) > 1:
                select.select_by_index(1)
                print("Selected country")
            else:
                print("No country options to select")

    def click_create_account_button(self):
        """Click the create account button"""
        # Just click the first button (which should be Create Account)
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        if buttons:
            buttons[0].click()
            print("Clicked Create Account button")
        else:
            print("No buttons found")

    def fill_create_account_form(self, first_name="Test", last_name="User", email="testuser@example.com", password="TestPassword123!", company_name="Test Company"):
        """Fill out the complete create account form"""
        print("Filling out the create account form...")
        
        # Fill each field one by one
        self.fill_first_name(first_name)
        time.sleep(1)
        
        self.fill_last_name(last_name)
        time.sleep(1)
        
        self.fill_email(email)
        time.sleep(1)
        
        self.fill_password(password)
        time.sleep(1)
        
        self.fill_company_name(company_name)
        time.sleep(1)
        
        self.fill_company_address1()
        time.sleep(1)
        
        self.fill_company_address2()
        time.sleep(1)
        
        self.fill_city()
        time.sleep(1)
        
        self.fill_zip_code()
        time.sleep(1)
        
        self.select_state()
        time.sleep(1)
        
        self.select_country()
        time.sleep(1)
        
        print("Form filled successfully!")
