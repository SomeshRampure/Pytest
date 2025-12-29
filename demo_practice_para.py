import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-save-password-bubble")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "autofill.profile_enabled": False,
    "autofill.credit_card_enabled": False,
    "autofill.address_enabled": False
})

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

# Login
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("9684")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("9684")
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button']"))).click()

# Verify login
if wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log Out"))):
    print("Login Successful")
else:
    print("Login Failed")

# Navigate to Accounts Overview
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Accounts Overview"))).click()

# Wait for table to be present and populated
table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
rows = table.find_elements(By.TAG_NAME, "tr")

# Extract and print data
for row in rows[1:]:  # Skip header row
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 3:
        account_id = cols[0].text
        balance = cols[1].text
        available_balance = cols[2].text
        print(f"Account ID: {account_id}, Balance: {balance}, Available Balance: {available_balance}")
    else:
        print("Row has fewer than 3 columns, skipping:", [col.text for col in cols])

# Logout
driver.find_element(By.LINK_TEXT, "Log Out").click()
driver.quit()
