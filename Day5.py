# import time
# from selenium import webdriver

# webdriver.Chrome()

# time.sleep(5)

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/")

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/")
# time.sleep(3)
# driver.minimize_window()

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.ID,"ta1").send_keys("Somesh Rampure")
# time.sleep(10)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.ID,"checkbox2").click()
# time.sleep(10)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(5)
# Text_ID = driver.find_element(By.ID,"textbox1")
# Text_ID.clear()
# time.sleep(5)
# Text_ID.send_keys("Somesh Rampure")
# time.sleep(5)
# Text_ID.clear()
# time.sleep(5)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(5)
# Text_Element = driver.find_element(By.ID,"pah").text
# print(Text_Element)
# driver.quit

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(5)
# Title_Page_One = driver.title
# print(Title_Page_One)
# driver.find_element(By.ID,"selenium143").click()
# time.sleep(5)
# Title_Page_Two = driver.title
# print(Title_Page_Two)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(5)
# driver.find_element(By.ID,"selenium143").click()
# time.sleep(5)
# Url_one = driver.current_url
# print(Url_one)

# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")

# time.sleep(15)
# driver.find_element(By.XPATH,"//span[text()='My Account']").click()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"Login").click()
# time.sleep(5)
# driver.find_element(By.ID,"input-email").clear()
# driver.find_element(By.ID,"input-email").send_keys("someshrampure9684@gmail.com")
# driver.find_element(By.ID,"input-password").clear()
# driver.find_element(By.ID,"input-password").send_keys("8888087087")
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
# time.sleep(5)
# if driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed():
#     print("Logged in successfully")
# else:
#     print("Login failed")
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
# time.sleep(5)
# driver.save_screenshot("login.png")
# driver.get_screenshot_as_file("Login2.png")

# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
# time.sleep(5)
# options = driver.find_elements(By.XPATH,"//select[@id='multiselect1']/option")
# for option in options :
#     print(options.text)


