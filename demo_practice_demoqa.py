from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Login
driver.get("https://demoqa.com/login")
wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.ID, "userName")))
username.send_keys("somesh")

password = driver.find_element(By.ID, "password")
password.send_keys("Somesh@8888")

login_button = driver.find_element(By.ID, "login")
login_button.click()

# Step 2: Navigate to Books page
driver.get("https://demoqa.com/books")

# Step 3: Search for book
search_box = wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
search_box.send_keys("Git Pocket Guide")

book = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Git Pocket Guide']")))
book.click()

# Step 4: Add book to collection
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add To Your Collection']")))
add_button.click()

# Step 5: Handle alert popup
alert = driver.switch_to.alert
alert.accept()

# Step 6: Navigate to Profile and verify book
driver.get("https://demoqa.com/profile")

# Verify presence of book in profile
book_in_profile = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Git Pocket Guide']")))
if book_in_profile:
    print("✅ Book successfully added to collection and verified in profile.")
else:
    print("❌ Book not found in profile.")

time.sleep(5)
driver.quit()