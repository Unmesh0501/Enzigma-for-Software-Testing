from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def validate_forgot_password():
    try:
        # Step 1: For the forgot password page
        driver.get('https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/forgot-password')

        # Step 2: For email field validate
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@title="Email"]'))
        )
        assert email_input.is_displayed(), "Email field is not displayed"
        
        # Step 3: Validate email format
        valid_email = "valid_email@example.com"
        invalid_email_format = "invalid-email.com"
        blank_email = ""
        
        # Test Case 1: Enter a valid email
        email_input.send_keys(valid_email)
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@title="Submit"]'))
        )
        submit_button.click()

        # Step 4: Check the success message for valid email
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Reset link sent to your email"]'))
        )
        print("Success: Reset link sent to your email.")
        
        # Step 5: Test with an invalid email
        email_input.clear()
        email_input.send_keys("nonregistered@example.com")
        submit_button.click()
        
        # Step 6: Check error message for invalid email
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="User does not exists"]'))
        )
        print("Error: User does not exists.")

        # Step 7: Test invalid email format
        email_input.clear()
        email_input.send_keys(invalid_email_format)
        submit_button.click()

        # Step 8: Check error message for invalid email format
        format_error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Please enter a valid email"]'))
        )
        print("Error: Please enter a valid email")

        # Step 9: Test blank email field
        email_input.clear()
        submit_button.click()

        # Step 10: Check error message for blank field
        blank_error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Please enter email"]'))
        )
        print("Error: Please enter email.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

validate_forgot_password()
