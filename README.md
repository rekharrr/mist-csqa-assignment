This assignment is designed to evaluate your ability to work with existing automation frameworks 
and extend them to add new test cases. 

You'll be working with a Python-based testing framework that involves API and UI automation using
pytest, requests, and Selenium.

## Assignment Objectives
1. Understand and navigate an existing test automation framework
2. Write new API and UI test cases following established patterns. 
3. Evaluate candidates code quality.  Please keep in mind coding practices like DRY (Do not repeat yourself), coding modularity and other software engineering principles. 
Your solution will be evaluated based on maintainability and reusability. 

NOTE - Feel free to use online documentation and other public resources, but the work must be your own.

## Initial Setup 
1. Have git installed (https://git-scm.com/downloads) 
2. Repo URL - https://github.com/rekharrr/mist-csqa-assignment/tree/main#
3. git clone https://github.com/rekharrr/mist-csqa-assignment.git


## Framework Overview

The framework is structured as follows:
```
mist-csqa-assignment/ # ENSURE YOUR DIRECTORY/PROJECT STRUCTURE STARTS HERE. ELSE YOU WILL GET IMPORT ERRORs. 
├── tests/ # API and UI test cases
├── libs/ # Base classes and shared logic
├── utils/ # Utility methods for API and UI automation
├── config/ # Configuration files
├── conftest.py # Pytest configurations and fixtures
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Prerequisites
- Python 3.x installed
- `pip` package manager installed
- Google Chrome browser installed
- [ChromeDriver](https://chromedriver.chromium.org/downloads) installed and added to your PATH


#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Running Tests
```bash
cd mist-csqa-assignment 
pytest -v tests/api_tests/org_api_tests.py (Example to run the Org API Tests)
```

## YOUR TASK

API Automation:
1. Automate the Sites API.
2. The API documentation for Sites can be found here : https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sites/create-org-site  (API URI is /api/v1/orgs/:org_id/sites).  
You can use the same payloads as in the example. Sample credentials are already present in the code. (With API token). 
3. You are expected to automate the following scenarios:
a) Create a Site with randomly generate name.
b) Update the Site name to another randomly generated name.
c) Delete the Site and verify the site is deleted. 

The same test cases for Org have already been automated in the framework. You can refer to them for guidance.
TODO files for site_api_libs and site_api_tests are already created in the framework. 

For UI Automation:
1. Automate the Create Account Test case with the following steps: 
a) Go to https://manage.ac2.mist.com/signin.html#!signup/register
b) Enter the details for various fields.
c) Click the "Create Account" button. (Note: A CAPTCHA may appear when you click the button. You can ignore this -- just verify that the button is clickable. The test ends at that point).

2. Sample test methods for navigating to the URL and ensuring we are on the right page have already been created in the framework.
You can refer to them for guidance. 

TODO placeholder for test_create_account is available in create_account_tests.py file. You can add any libs in the create_account_libs.py file as required.


### SUBMISSION 

Once complete, Please submit the PR to the same repository and send the PR link on the same email thread in which the assignment was mailed to you. 
(or) Send the Zip file of the finished assignment (code) to us on the same email thread in which the assignment was mailed to you.


Thanks! 
