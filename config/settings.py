### configs/settings.py
"""Configuration settings for the test framework."""
import os

class Config:
    """Base configuration class."""

    # API Configuration
    BASE_URL = os.getenv('BASE_URL', 'https://api.ac2.mist.com/api/v1')
    UI_BASE_URL = os.getenv('UI_BASE_URL', 'https://manage.ac2.mist.com')

    # Authentication
    USERNAME = os.getenv('USERNAME', 'testcoding@assignment.com')
    PASSWORD = os.getenv('PASSWORD', 'testcoding@assignment.com')
    API_TOKEN = os.getenv('API_TOKEN', 'Gs0iQefxuWS2DwIQDgOh6Ke3ZhB1jgqJOE5Qnj0E6UNAa0QaPE6EJTlidKM19cpsfpHJ1E3ChUTwtn3hcDkEAZNaVI4l9QwG')

    # Test Configuration
    TIMEOUT = int(os.getenv('TIMEOUT', '30'))
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))

    # Browser Configuration
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'

    # Reporting
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_DIR = 'screenshots'