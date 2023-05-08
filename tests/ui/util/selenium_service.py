from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumService:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def openURL(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver
    
    def wait_until_located(self, locator, locator_type=By.XPATH):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator))
        )

    def find_element(self, locator, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator)
