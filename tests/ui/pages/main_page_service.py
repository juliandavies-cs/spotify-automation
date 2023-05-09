import pytest

class MainPage:
    def __init__(self):
        self.login_button_locator = "//button[@data-testid='login-button']"
        self.logged_in_user_name_locator= "//span[@data-testid='user-widget-name']"
        self.create_playlist_button_locator = "//button[@data-testid='create-playlist-button']"

    def login(self, test_case):
        login_button = test_case.selenium_service.wait_until_located(self.login_button_locator)
        login_button.click()
    
    def verify_successful_login(self, test_case, username):
        try:
            test_case.selenium_service.wait_until_located(self.logged_in_user_name_locator)
            assert test_case.selenium_service.find_element(self.logged_in_user_name_locator).text == username
        except Exception as e:
            pytest.fail(f"Failed with exception: {type(e).__name__}")

    def create_playlist(self, test_case, playlist_name):
        create_playlist_button = test_case.selenium_service.wait_until_located(self.create_playlist_button_locator)
        create_playlist_button.click()
        test_case.playlist_page.rename_playlist(test_case, playlist_name)
