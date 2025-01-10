from selenium import webdriver

driver = webdriver.Chrome()

# For Open the noKodr platform
driver.get("https://app-staging.nokodr.com/")

driver.implicitly_wait(5)
driver.quit()
