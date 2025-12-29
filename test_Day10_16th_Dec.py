import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
# print(driver.title)
# element = driver.find_element(By.LINK_TEXT, "Page One")
# element1 = driver.find_element(By.ID, "selenium143")
# print("Text of link 1 : " + element1.text)
# element2 = driver.find_element(By.CLASS_NAME, "home-link")
# print("Text of link 2 : " + element2.text)
# element3 = driver.find_element(By.CLASS_NAME, "feed-link")
# print("Text of link 3 : " + element3.text)

# links = driver.find_elements(By.TAG_NAME, "a")

# print("Total number of links on the page : " + str(len(links)))
# for i, link in enumerate(links):
#     print(f"link {i+1}: {link.text}")

# table = driver.find_element(By.ID, "table1")

# rows = table.find_elements(By.XPATH, ".//tbody/tr")

# for row in rows :
#     cells = row.find_elements(By.TAG_NAME, "td")
#     if len(cells)>= 3:
#         name = cells[0].text
#         age = cells[1].text
#         place = cells[2].text
#         print(f"Name : {name}, Age = {age}, Place = {place}")

# print("Total number of rows in the table : " + str(len(rows)))

# time.sleep(3)
# driver.quit()


