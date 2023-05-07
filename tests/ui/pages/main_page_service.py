from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self) -> None:
        self.login_button_locator = "//button[@data-testid='login-button']"

    def login(self, driver):
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.login_button_locator))
        )
        login_button.click()