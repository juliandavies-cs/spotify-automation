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

    def get_song_locator_based_on_count(self, count):
        return f"//div[@aria-rowindex='{count+2}']" 
    
    def delete_playlist(self, test_case):
        test_case.selenium_service.wait_until_located(self.more_button_locator).click()
        test_case.selenium_service.wait_until_located(self.delete_button_locator).click()
        test_case.main_page.delete_playlist(test_case)

    def verify_songs_added(self, test_case, playlist_songs):
        try:
            for idx, song in enumerate(playlist_songs):
                song_locator = self.get_song_locator_based_on_count(idx)
                test_case.selenium_service.wait_until_located(f"{song_locator}/div/div[2]/div/a/div")
                assert test_case.selenium_service.find_element(f"{song_locator}/div/div[2]/div/a/div").text == song['title']
                assert test_case.selenium_service.find_element(f"{song_locator}/div/div[2]/div/span/a").text == song['artist']
        except Exception as e:
            pytest.fail(f"Failed with exception: {type(e).__name__}")

