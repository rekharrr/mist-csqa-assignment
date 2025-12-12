import pytest
import logging
from datetime import datetime
from libs.ui_libs.todo_create_account_libs import CreateAccountLibs
from utils.ui_utils.ui_utils import UIUtils


class TestCreateAccount:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        try:
            self.driver = UIUtils.get_driver()
            self.create_account = CreateAccountLibs(self.driver)
            yield

        except Exception as e:
            print(f"Setup failed: {e}")
            raise
        finally:
            # Cleanup after test - ensure driver exists before quitting
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()

    def test_navigate_to_create_account(self):
        """Test navigation to create account page"""
        try:
            self.create_account.navigate_to_create_account_page()

            # Verify we're on the correct page
            current_url = self.driver.current_url
            assert "signup/register" in current_url, "{} :: Failed to navigate to create account page. Current URL: {current_url}"
            print("Navigation test passed!")

        except Exception as e:
            # Take screenshot for debugging
            if hasattr(self, 'driver') and self.driver:
                try:
                    screenshot_path = self.create_account.ui_utils.take_screenshot("navigation_error.png")
                    print(f"Screenshot saved: {screenshot_path}")
                except:
                    pass
            pytest.fail(f"Navigation test failed: {str(e)}")

    def test_page_title(self):
        """Additional test to verify page loads correctly"""
        try:
            self.create_account.navigate_to_create_account_page()

            # Wait for page to load
            import time
            time.sleep(3)

            page_title = self.driver.title
            print(f"Page title: {page_title}")

            # Verify page title is not empty
            assert page_title, "Page title is empty"

        except Exception as e:
            pytest.fail(f"Page title test failed: {str(e)}")


    def test_create_account(self):
        """
        Test to create an account by filling the form and clicking Create Account button.
        Note: CAPTCHA may be triggered - test ends after clicking the button.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_create_account"))
        
        try:
            # Generate unique email using timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            test_email = f"test.user.{timestamp}@example.com"
            
            # Test data
            first_name = "Test"
            last_name = "User"
            password = "TestPassword123!"
            
            logging.info(f"Creating account with email: {test_email}")
            
            # Navigate to create account page
            self.create_account.navigate_to_create_account_page()
            
            # Verify we're on the correct page
            current_url = self.driver.current_url
            assert "signup/register" in current_url, f"Failed to navigate to create account page. Current URL: {current_url}"
            
            # Fill the form
            self.create_account.fill_create_account_form(first_name, last_name, test_email, password)
            
            # Wait a moment for form to be ready
            import time
            time.sleep(1)
            
            # Click Create Account button
            self.create_account.click_create_account_button()
            
            logging.info("Successfully clicked Create Account button")
            logging.info("Note: CAPTCHA may be triggered at this point")
            
            # Wait to see if CAPTCHA or success page appears
            time.sleep(3)
            
            # Test passes if we successfully clicked the button
            print("Create account test passed - button was clicked successfully!")
            
        except Exception as e:
            # Take screenshot for debugging
            if hasattr(self, 'driver') and self.driver:
                try:
                    screenshot_path = self.create_account.ui_utils.take_screenshot("create_account_error.png")
                    print(f"Screenshot saved: {screenshot_path}")
                except:
                    pass
            pytest.fail(f"Create account test failed: {str(e)}")