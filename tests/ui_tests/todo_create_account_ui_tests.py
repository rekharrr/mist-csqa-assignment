import pytest
from libs.ui_libs.create_account_libs import CreateAccountLibs
from utils.ui_utils.ui_utils import UIUtils  # Fixed import path


class TestCreateAccount:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        try:
            self.driver = UIUtils.get_driver()
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


    # TODO : Add test case to enter details and create the account.
    # Add any Libs as needed in todo_create_account_libs.py and use them here.
    # def test_create_account(self):