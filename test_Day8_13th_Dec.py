import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_teardown")
class TestSearch:

    def test_search_HP_laptop(self):
        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065")

    @pytest.mark.smoke
    def test_search_empty_text(self):
        self.driver.find_element(By.NAME,"search")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_test = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_test)
    