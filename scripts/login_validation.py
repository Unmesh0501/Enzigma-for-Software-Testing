from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def validate_login_fields():
    try:
        # Step 1: For the login page
        driver.get('https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login')

        # Step 2: For the fields (username and password)
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@title="Email"]'))
        )
        assert email_input.is_displayed(), "Email field is not displayed"
        
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@title="Password"]'))
        )
        assert password_input.is_displayed(), "Password field is not displayed"
        
        # Step 3: Check password and email input
        email_input.send_keys('patilunmesh58@gmail.com')
        password_input.send_keys('Unmesh@1234')
        
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@title="Login"]'))
        )
        login_button.click()

        # Step 4: For the login (valid credentials)
        WebDriverWait(driver, 20).until(
            EC.url_contains('dashboard')
        )
        print("Login with valid credentials was successful.")

        # Step 5: Test invalid credentials (wrong password)
        email_input.clear()
        password_input.clear()
        email_input.send_keys('valid_email@example.com')
        password_input.send_keys('WrongPassword')
        login_button.click()

        # Step 6: Verify the error message for invalid credentials
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Invalid username or password"]'))
        )
        print("Error message displayed for invalid credentials.")

        # Step 7: Testing blank fields
        email_input.clear()
        password_input.clear()
        login_button.click()

        # Step 8: Verify error message for blank fields
        blank_error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Please enter your username and password"]'))
        )
        print("Error message displayed for blank fields.")

        # Step 9: For test special characters
        email_input.clear()
        password_input.clear()
        email_input.send_keys('!@#$%^&*()')
        password_input.send_keys('!@#$%^&*()')
        login_button.click()

        # Step 10: Verify error message for special characters
        special_char_error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Invalid username or password"]'))
        )
        print("Error message displayed for special characters.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

validate_login_fields()
