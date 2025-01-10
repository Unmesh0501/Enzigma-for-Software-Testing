# NoKodr Platform Automation

This repository contains automation scripts for validating signup, login, and forgot password functionalities of the NoKodr platform using Selenium with Python.

Before running the scripts, make sure you have the following installed:
Python 3.13.1
python -m venv venv
.\venv\Scripts\activate
pip install selenium


Troubleshooting:- 
If you encounter any issues during script execution, refer to the following tips:

1) Chrome Browser Issues: Ensure Google Chrome is installed and updated on your system.

2) Driver Mismatch: 
The scripts use webdriver-manager to fetch the appropriate chromedriver. If you experience errors, try updating the manager:
pip install selenium webdriver-manager

3) Dependency Issues: Reinstall required libraries:
pip install -r requirements.txt



Features of the Automation Scripts:-

1) Signup Validation:   
Tests OTP-based signup flow.
Handles validations for mandatory fields and edge cases (e.g., invalid OTPs).
Verifies successful account creation.

2) Login Validation:
Validates mandatory fields (username and password).
Tests for valid and invalid login credentials.
Handles special characters, blank fields, and incorrect inputs.
Ensures successful redirection to the dashboard upon valid credentials.

4) Forgot Password Validation:
Validates the email field for mandatory and format constraints.
Tests system responses for registered, non-registered, and invalid email inputs.
Verifies error or success messages for each scenario.



## How to Run the Automation Scripts

1. Verify Environment Setup
python scripts/basic_script.py

2. Signup Validation
python scripts/signup_validation.py

3. Login Validation
python scripts/login_validation.py

4. Forgot Password Validation
python scripts/forgot_password_validation.py



Why This Project is Important:
Real-World Application: Automates critical user workflows like signup, login, and password recovery.
Comprehensive Testing: Covers positive and negative test cases, ensuring robust validation.
Showcases Automation Skills: Demonstrates expertise in Selenium, Python, and test automation best practices.

