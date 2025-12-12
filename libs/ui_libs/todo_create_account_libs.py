from utils.ui_utils.ui_utils import UIUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

class CreateAccountLibs:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ui_utils = UIUtils(driver)

    def navigate_to_create_account_page(self):
        """Navigate to the create account page"""
        self.ui_utils.navigate_to("https://manage.ac2.mist.com/signin.html#!signup/register")
        # Wait for page to load and form elements to be present
        time.sleep(3)

    def enter_first_name(self, first_name: str):
        """Enter first name in the form"""
        logging.info(f"Entering first name: {first_name}")
        try:
            # Try multiple locator strategies
            self.ui_utils.send_keys(By.NAME, "firstName", first_name)
        except:
            raise Exception("First Name field not found")

    def enter_last_name(self, last_name: str):
        """Enter last name in the form"""
        logging.info(f"Entering last name: {last_name}")
        try:
            self.ui_utils.send_keys(By.NAME, "lastName", last_name)
        except:
            raise Exception("Last Name field not found")

    def enter_email(self, email: str):
        """Enter email in the form"""
        logging.info(f"Entering email: {email}")
        try:
            self.ui_utils.send_keys(By.NAME, "email", email)
        except:
            raise Exception("Email field not found")

    def enter_password(self, password: str):
        """Enter password in the form"""
        logging.info("Entering password")
        try:
            self.ui_utils.send_keys(By.NAME, "password", password)
        except:
            raise Exception("Password field not found")

    def enter_company_name(self, company_name: str):
        """Enter company name in the form"""
        logging.info("Entering company name")
        try:
            self.ui_utils.send_keys(By.NAME, "companyName", company_name)
        except:
            raise Exception("Company Name field not found")

    def enter_company_address_1(self, company_address_1: str):
        """Enter company address 1 in the form"""
        logging.info("Entering company address 1")
        try:
            self.ui_utils.send_keys(By.NAME, "data-input-field", company_address_1)
            time.sleep(1)
            self.ui_utils.click_element(By.XPATH, "(//*[contains(text(),'Spain')])[1]")
        except:
            raise Exception("Company Address 1 field not found")
    
    def enter_company_address_2(self, company_address_2: str):
        """Enter company address 2 in the form"""
        logging.info("Entering company address 2")
        try:
            self.ui_utils.send_keys(By.NAME, "companyAddress2", company_address_2)
        except:
            raise Exception("Company Address 2 field not found")

    def enter_city(self, city: str):
        """Enter city in the form"""
        logging.info("Entering city")
        try:
            self.ui_utils.send_keys(By.NAME, "city", city)
        except:
            raise Exception("City field not found")
    
    def enter_state(self, state: str):
        """Enter state in the form"""
        logging.info("Entering state")
        try:
            self.ui_utils.click_element(By.XPATH, "//*[@class='signup-select']")
            time.sleep(1)
            self.ui_utils.click_element(By.XPATH, "//*[contains(text(),'Alicante')]")
        except:
            raise Exception("State field not found")

    def enter_zip_code(self, zip_code: str):
        """Enter zip code in the form"""
        logging.info("Entering zip code")
        try:
            self.ui_utils.send_keys(By.NAME, "zipCode", zip_code)
        except:
            raise Exception("Zip code field not found")

    def check_terms_and_conditions(self):
        """Check the terms and conditions checkbox"""
        logging.info("Checking terms and conditions checkbox")
        try:
            self.ui_utils.click_element(By.XPATH, "//*[@class='uikit-checkbox-icon-container']/span")

        except Exception as e:
            logging.warning(f"Could not check terms checkbox: {e}. Continuing anyway...")

    def click_create_account_button(self):
        """Click the Create Account button"""
        logging.info("Clicking Create Account button")
        try:
            # Wait a moment for button to be ready
            time.sleep(1)
            
            # Try multiple strategies to find and click the button
            try:
                self.ui_utils.click_element(By.XPATH, "//span[contains(text(),'Create Account')]")
            except:
                raise Exception("Create Account button not found")
        except Exception as e:
            logging.error(f"Failed to click button: {e}")
            raise

    def fill_create_account_form(self, first_name: str, last_name: str, email: str, password: str):
        """Fill all fields in the create account form"""
        logging.info("Filling create account form")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_company_name("Test Company")
        self.enter_company_address_1("Spain")
        self.enter_company_address_2("Suite 100")
        self.enter_city("Test City")
        self.enter_state("Alicante")
        self.enter_zip_code("12345")
        self.check_terms_and_conditions()

    def create_account(self, first_name: str, last_name: str, email: str, password: str):
        """Complete flow to create an account"""
        logging.info("Starting account creation process")
        self.navigate_to_create_account_page()
        self.fill_create_account_form(first_name, last_name, email, password)
        self.click_create_account_button()
        logging.info("Account creation button clicked - CAPTCHA may appear")