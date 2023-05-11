from ui.util.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumService:
    def __init__(self):
        self.driver = driver
        
    def open_url(self, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver
    
    def close(self):
        self.driver.close()

    def wait_until_located(self, locator, locator_type=By.XPATH):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator))
        )
    
    def wait_until_element_text_to_be(self, locator, text, locator_type=By.XPATH, ):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((locator_type, locator), text)
        )

    def find_element(self, locator, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator)
    
    def hover_over_element(self, locator, locator_type=By.XPATH):
        a = ActionChains(self.driver)
        element = self.find_element(locator, locator_type)
        a.move_to_element(element).perform()
