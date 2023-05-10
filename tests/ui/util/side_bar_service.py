import pytest


class SideBar:
    def __init__(self):
        self.playlist_text_sidebar_locator = "//p[contains(@id, 'listrow-title-spotify:playlist')]/span"
        self.playlist_btn_locator = "//p[contains(@id, 'listrow-title-spotify:playlist')]/../../../button"
        self.search_btn = "//a[@href='/search']"

    def click_search(self, test_case):
        test_case.selenium_service.find_element(self.search_btn).click()

    def click_playlist(self, test_case):
        test_case.selenium_service.wait_until_element_text_to_be(self.playlist_text_sidebar_locator, "My Playlist #1")
        test_case.selenium_service.find_element(self.playlist_btn_locator).click()

    def verify_playlist_created(self, test_case):
        test_case.selenium_service.wait_until_element_text_to_be(self.playlist_text_sidebar_locator, "My Playlist #1")
        return True