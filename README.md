This assignment is designed to evaluate your ability to work with existing automation frameworks 
and extend them to add new test cases. 

You'll be working with a Python-based testing framework that involves API and UI automation using
pytest, requests, and Selenium.

## Pre-requisites 
1. GitHub account (https://github.com/join)
2. Install Git CLI  (https://git-scm.com/downloads) 
3. Install Python 3.9.6 (https://www.python.org/downloads)
4. Google Chrome browser (https://www.google.com/chrome)
5. Familiarize yourself with basics of Pytest (https://docs.pytest.org/en/stable) 
6. Familiarize yourself with basics of Selenium (https://www.selenium.dev/documentation/webdriver)

## Assignment Objectives
1. Understand and navigate an existing test automation framework.
2. Write new API and UI test cases following established patterns. 
3. Ensure good code quality. Please keep in mind coding practices like DRY (Don't Repeat Yourself), coding modularity, and other software engineering principles.
Your solution will be evaluated based on maintainability and reusability.

NOTE - Feel free to use online documentation and other public resources, but the work must be your own.

## Steps to setup the framework 

### Clone the repository 
```sh
git clone https://github.com/rekharrr/mist-csqa-assignment.git
```

### Setup Virtual Environment and Install Dependencies

##### Linux / macOS
```sh
cd mist-csqa-assignment         # Navigate to the project directory. 
python3 -m venv venv            # Create a virtual environment
source venv/bin/activate        # Activate the virtual environment (Linux/macOS)
pip install -r requirements.txt # Install required packages
```

##### Windows (PowerShell)
```sh
cd mist-csqa-assignment
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Run Existing Tests to Ensure the Setup is Correct
```sh
cd mist-csqa-assignment                    # Navigate to the project directory. 
pytest -v tests/api_tests/org_api_tests.py # Run existing Org API tests
```

On executing the tests, you should see output indicating that the tests have passed successfully.
```sh
tests/api_tests/org_api_tests.py::TestOrgAPI::test_01_create_org PASSED
tests/api_tests/org_api_tests.py::TestOrgAPI::test_02_update_org PASSED
tests/api_tests/org_api_tests.py::TestOrgAPI::test_03_delete_org PASSED
```

## Framework Overview
The framework is structured as follows:
```sh
mist-csqa-assignment/ # ENSURE YOUR DIRECTORY/PROJECT STRUCTURE STARTS HERE. ELSE YOU WILL GET IMPORT ERRORs. 
├── tests/            # API and UI test cases
├── libs/             # Base classes and shared logic
├── utils/            # Utility methods for API and UI automation
├── config/           # Configuration files
├── conftest.py       # Pytest configurations and fixtures
├── requirements.txt
└── README.md
```

## TASKS

### Task 1 - API Automation for Sites API. 

#### BACKGROUND:
When a user creates an account in the Mist Cloud, they can then create Organizations (Orgs), and later, Sites within those Orgs. 
These act as logical groupings -- users can manage multiple Orgs, and each Org can contain multiple Sites. 
Both Orgs and Sites can be created, updated, and deleted via Mist APIs. 
For the purpose of this assignment, we will not go into too much detail about Orgs and Sites. 

#### YOUR TASK : Automate the CRUD operations for Sites API.
1. Refer to the existing Org API automation code in `org_api_libs.py` and `org_api_tests.py` files for reference. 
2. Similar to them, update `todo_site_api_libs.py` and `todo_site_api_tests.py` files to automate the Site API test cases. 
3. Cover the following test cases for Site API: <br>
a) Create a Site with a randomly generated name. <br>
b) Update the Site name to a different randomly generated name. <br>
c) Delete the Site and verify the site is deleted. <br>

The API documentation for Sites can be found here: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sites/create-org-site (API URI is /api/v1/orgs/:org_id/sites). <br> 
You can use the same payloads as in the example. Sample credentials are already present in the code. (With API token). <br> 

### Task 2 - UI Automation for Create Account Page.

#### BACKGROUND:
Users can create accounts on the Mist platform via the Create Account page: https://manage.ac2.mist.com/signin.html#!signup/register 

#### YOUR TASK : Automate the Create Account Page test case using Selenium. <br>
1. Update the `todo_create_account_tests.py` and `todo_create_account_libs.py` files to automate a test case with the below steps: <br>
a) Go to https://manage.ac2.mist.com/signin.html#!signup/register <br>
b) Enter the details for the various fields. <br>
c) Click on the Create Account button. <br>

(Note: Sometimes CAPTCHA is triggered when clicking the Create Account button. You can ignore the CAPTCHA -- just ensure that you are able to click on the Create Account button, and the test ends there.) <br>

### SUBMISSION
Once complete, please submit a pull request (PR) to this repository and reply to the original email thread (where you received this assignment) with the PR link. 
(For instructions on how to create a PR, please refer to: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=webui)

Thanks! 
