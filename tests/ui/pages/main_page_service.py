import pytest

class MainPage:
    def __init__(self):
        self.login_button_locator = "//button[@data-testid='login-button']"
        self.logged_in_user_name= "//span[@data-testid='user-widget-name']"

    def login(self, test_case):
        login_button = test_case.selenium_service.wait_until_located(self.login_button_locator)
        login_button.click()
    
    def verify_successful_login(self, test_case, username):
        try:
            test_case.selenium_service.wait_until_located(self.logged_in_user_name)
            assert test_case.selenium_service.find_element(self.logged_in_user_name).text == username
        except Exception as e:
            pytest.fail(f"Failed with exception: {type(e).__name__}")
