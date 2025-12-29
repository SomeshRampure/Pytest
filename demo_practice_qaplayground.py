import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

####################INPUT FIELDS DEMO ON QA PLAYGROUND####################

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.qaplayground.com/practice")

# input = driver.find_element(By.XPATH, "(//div/a/span)[2]")
# input.click()
# time.sleep(5)

# movie_name = driver.find_element(By.ID, "movieName")
# movie_name.send_keys("Inception")
# time.sleep(5)

# append_text = driver.find_element(By.ID, "appendText")
# append_text.send_keys(" - Directed by Christopher Nolan")
# time.sleep(5)

# present_text = driver.find_element(By.ID, "insideText")
# present_text_value = present_text.get_attribute("value")
# print ("Present Text Value:", present_text_value)

# clear_text = driver.find_element(By.ID, "clearText")
# clear_text.clear()
# time.sleep(5)

# disabled_text = driver.find_element(By.ID, "disabledInput")
# is_disabled = disabled_text.get_attribute("disabled") == "true"
# if is_disabled:
#     print("Disabled")
# else: 
#     print("Enabled")
# time.sleep(5)

# read_only = driver.find_element(By.ID, "readonlyInput")
# is_readonly = read_only.get_attribute("readonly")=="true"
# if is_readonly:
#     print("Read-Only")      
# else:
#     print("Editable")
# time.sleep(5)

# driver.quit()


####################BUTTON FIELDS DEMO ON QA PLAYGROUND####################

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qaplayground.com/practice")
time.sleep(5)

button_click = driver.find_element(By.XPATH, "(//div/a/span)[3]")
button_click.click()
time.sleep(5)

go_to_home= driver.find_element(By.ID, "button-color")
go_to_home.click()
time.sleep(5)

get_started = driver.find_element(By.LINK_TEXT, "Get Started")
get_started.click()
time.sleep(5)

button_click.click()
