from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self) -> None:
        self.username_input_locator = "//input[@id='login-username']"
        self.password_input_locator = "//input[@id='login-password']"
        self.login_button_locator = "//button[@id='login-button']"

    def login(self, driver, username, password):
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_input_locator))
        )
        username_input.send_keys(username)
        password_input = driver.find_element(By.XPATH, self.password_input_locator)
        password_input.send_keys(password)
        login_button_account_page = driver.find_element(By.XPATH, self.login_button_locator)
        login_button_account_page.click()