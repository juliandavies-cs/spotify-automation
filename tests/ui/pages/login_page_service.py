class LoginPage:
    def __init__(self) -> None:
        self.username_input_locator = "//input[@id='login-username']"
        self.password_input_locator = "//input[@id='login-password']"
        self.login_button_locator = "//button[@id='login-button']"

    def login(self, test_case, username, password):
        username_input = test_case.selenium_service.wait_until_located(self.username_input_locator)
        username_input.send_keys(username)
        password_input = test_case.selenium_service.find_element(self.password_input_locator)
        password_input.send_keys(password)
        login_button_account_page = test_case.selenium_service.find_element(self.login_button_locator)
        login_button_account_page.click()