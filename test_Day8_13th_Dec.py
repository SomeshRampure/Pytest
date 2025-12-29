import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType  # ✅ Required for screenshot attachment

@pytest.mark.usefixtures("test_setup_and_teardown")
class TestSearch:

    def test_search_HP_laptop(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default']").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065")
        allure.attach(self.driver.get_screenshot_as_png(), name="HP", attachment_type=AttachmentType.PNG)

@pytest.mark.smoke
def test_search_empty_text(self):
        self.driver.find_element(By.NAME, "search").clear()
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default']").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='content']/p").text
        assert actual_text == expected_text