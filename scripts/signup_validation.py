from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: For open signup page
    driver.get('https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/signup')

    # Step 2: For the email field 
    email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@title="Email"]'))
    )
    email_input.send_keys('patilunmesh58@gmail.com')

    # Step 3: For click procees button
    sign_up_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@title="Proceed"]'))
    )
    sign_up_button.click()

    # Step 4: For OTP input field
    otp_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@title="Verification Code"]'))
    )
    otp_input.send_keys('123456')  # Replace when otp generate

    # Step 5: For the fields to appear after OTP verification (First Name, Last Name, Password and Confirm Password )
    first_name_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@name="firstName"]'))
    )
    first_name_input.send_keys('Unmesh')

    last_name_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@name="lastName"]'))
    )
    last_name_input.send_keys('Patil')

    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@name="password"]'))
    )
    password_input.send_keys('Unmesh@1234')

    confirm_password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@name="password-confirmPassword"]'))
    )
    confirm_password_input.send_keys('Unmesh@1234')

    # Step 6: Submit the registration form
    register_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Register"]'))
    )
    register_button.click()

    # Step 7: Wait for success message and validate
    success_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[text()="Account created successfully!"]'))
    )
    print("Signup process completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
