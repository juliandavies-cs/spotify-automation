import pytest


class SideBar:
    def __init__(self):
        self.playlist_text_sidebar_locator = "//li[@data-testid='rootlist-item']/a/span[1]"
        self.search_btn = "//a[@href='/search']"

    def verify_playlist_name(self, test_case, playlist_name):
        try:
            actual_name_element = test_case.selenium_service.wait_until_located(self.playlist_text_sidebar_locator)
            actual_playlist_name = actual_name_element.text
            assert actual_playlist_name == playlist_name
        except Exception as e:
            pytest.fail(f"Failed with exception: {type(e).__name__}")

    def click_search(self, test_case):
        test_case.selenium_service.find_element(self.search_btn).click()