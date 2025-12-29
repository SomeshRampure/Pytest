

# from selenium import webdriver

# import time


# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# print(driver.title)



# time.sleep(3)
# driver.quit()


# 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
    
    # Find and fill username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    
    # Find and fill password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    # YOUR CODE HERE
    
    # Find and click login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    # YOUR CODE HERE
    
    print("✅ Login action completed!")
    
    time.sleep(3)

finally:
    driver.quit()

