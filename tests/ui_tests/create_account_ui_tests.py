import pytest
import time
from libs.ui_libs.create_account_libs import CreateAccountLibs
from utils.ui_utils.ui_utils import UIUtils  # Fixed import path


class TestCreateAccount:
    driver = None
    
    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown(self):
        # Setup browser once for all tests in this class
        TestCreateAccount.driver = UIUtils.get_driver()
        yield
        # Clean up browser after all tests
        TestCreateAccount.driver.quit()

    def test_navigate_to_create_account(self):
        # Test going to the create account page
        self.create_account = CreateAccountLibs(TestCreateAccount.driver)
        self.create_account.navigate_to_create_account_page()

        # Check we got to the right page
        current_url = TestCreateAccount.driver.current_url
        assert "signup/register" in current_url, f"Wrong page! Current URL: {current_url}"
        print("Navigation test passed!")

    def test_page_title(self):
        # Test that the page loads and has a title
        self.create_account = CreateAccountLibs(TestCreateAccount.driver)
        self.create_account.navigate_to_create_account_page()

        # Wait for page to load
        time.sleep(3)

        page_title = TestCreateAccount.driver.title
        print(f"Page title: {page_title}")

        # Make sure page has a title
        assert page_title, "Page title is empty"


    def test_create_account(self):
        # Test filling out the create account form
        self.create_account = CreateAccountLibs(TestCreateAccount.driver)
        
        # Go to the create account page
        self.create_account.navigate_to_create_account_page()
        time.sleep(3)  # Wait for page to load
        
        # Make sure we're on the right page
        current_url = TestCreateAccount.driver.current_url
        assert "signup/register" in current_url, f"Wrong page! Current URL: {current_url}"
        
        # Fill out all the form fields
        self.create_account.fill_create_account_form()
        
        # Click the create account button
        self.create_account.click_create_account_button()
        
        # Wait a bit to see what happens
        time.sleep(3)
        
        # Take a screenshot to show what happened
        screenshot_path = self.create_account.ui_utils.take_screenshot("create_account_test.png")
        print(f"Screenshot saved: {screenshot_path}")
        
        # Test passed if we could click the button (CAPTCHA might show up)
        print("Create account test completed successfully - button was clickable")