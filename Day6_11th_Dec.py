# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(2)
# drop_down = driver.find_element(By.ID,"drop1")
# select = Select(drop_down)
# select.select_by_visible_text("doc 3")
# time.sleep(2)
# select.select_by_value("mno")
# time.sleep(2)
# select.select_by_index(2)
# time.sleep(2)

# multiple_drop_down = driver.find_element(By.ID,"multiselect1")
# select = Select(multiple_drop_down)
# select.select_by_visible_text("Volvo")
# select.select_by_value("audix")
# select.select_by_index(2)

# select.deselect_by_value("volvox")
# select.deselect_by_index(3)
# select.select_by_visible_text("Hyundai")

# select.deselect_all
# time.sleep(3)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains, Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")

# time.sleep(3)

# actions = ActionChains(driver)
# sele_143 = driver.find_element(By.ID,"link1")
# actions.click(sele_143).perform()

# time.sleep(3)

# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")

# parent_window = driver.current_window_handle
# driver.find_element(By.LINK_TEXT,"Open a popup window").click()

# windows = driver.window_handles

# time.sleep(3)

# for w in windows:
#     driver.switch_to.window(w)
#     if driver.title.__eq__("Basic Web Page Title"):
#         para_one_text = driver.find_element(By.ID,"para1").text
#         print(para_one_text)
#         driver.close()
#         break

# time.sleep(3)

# driver.switch_to.window(parent_window)
# driver.find_element(By.ID,"ta1").send_keys("Somesh rampure")
# time.sleep(3)
# driver.close() 