class MainPage:
    def __init__(self):
        self.login_button_locator = "//button[@data-testid='login-button']"

    def login(self, test_case):
        login_button = test_case.selenium_service.wait_until_located(self.login_button_locator)
        login_button.click()