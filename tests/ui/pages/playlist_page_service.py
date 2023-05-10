import pytest
import time

class PlaylistPage:
    def __init__(self):
        self.playlist_name_btn_locator = "//span[@data-testid='entityTitle']/button"
        self.edit_playlist_name_input_locator = "//input[@data-testid='playlist-edit-details-name-input']"
        self.edit_playlist_save_btn_locator = "//button[@data-testid='playlist-edit-details-save-button']"
        self.more_button_locator = "//button[@data-testid='more-button']"
        self.delete_button_locator = "//span[text()='Delete']/.."

    """UNUSED"""
    def rename_playlist(self, test_case, playlist_name):
        playlist_name_btn = test_case.selenium_service.wait_until_located(self.playlist_name_btn_locator)
        playlist_name_btn.click()
        playlist_name_input = test_case.selenium_service.wait_until_located(self.edit_playlist_name_input_locator)
        playlist_name_input.send_keys(playlist_name)
        test_case.selenium_service.find_element(self.edit_playlist_save_btn_locator).click()

    def delete_playlist(self, test_case):
        test_case.selenium_service.wait_until_located(self.more_button_locator).click()
        test_case.selenium_service.wait_until_located(self.delete_button_locator).click()
        test_case.main_page.delete_playlist(test_case)

