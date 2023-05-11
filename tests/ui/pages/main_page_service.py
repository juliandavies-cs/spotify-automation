import pytest

from selenium.webdriver.common.keys import Keys
from ui.util.selenium_service import SeleniumService
from ui.util.side_bar_service import SideBar


class MainPage:

    def __init__(self):
        self.selenium_service = SeleniumService()
        self.side_bar_service = SideBar()

        self.login_button_locator = "//button[@data-testid='login-button']"
        self.logged_in_user_name_locator= "//span[@data-testid='user-widget-name']"
        self.create_playlist_button_locator = "//span[text()='Create playlist']/.."
        self.search_bar_locator = "//input[@data-testid='search-input']"
        self.delete_playlist_button_locator = "//span[text()='Delete']/.."
        self.first_song_title_locator = "//div[@aria-rowindex='1']/div/div/div[2]/a/div"
        self.first_song_artist_locator = "//div[@aria-rowindex='1']/div/div/div[2]/span/a"
        self.first_song_options_locator = "//div[@aria-rowindex='1']/div/div[2]/button[2]"
        self.add_to_playlist_locator = "//span[text()='Add to playlist']/.."
        self.add_to_playlist_btn_locator = "//li/button/span[text()='My Playlist #1']/.."

    def login(self):
        login_button = self.selenium_service.wait_until_located(
            self.login_button_locator)
        login_button.click()

    def verify_successful_login(self, username):
        try:
            self.selenium_service.wait_until_located(
                self.logged_in_user_name_locator)
            assert self.selenium_service.find_element(
                self.logged_in_user_name_locator).text == username
        except Exception as e:
            pytest.fail(f"Failed with exception: {type(e).__name__}")

    def create_playlist(self):
        create_playlist_button = self.selenium_service.wait_until_located(
            self.create_playlist_button_locator)
        create_playlist_button.click()

    def delete_playlist(self):
        delete_playlist_button = self.selenium_service.wait_until_located(
            self.delete_playlist_button_locator)
        delete_playlist_button.click()

    def search_for_song(self, song):
        self.side_bar_service.click_search()
        search_bar = self.selenium_service.wait_until_located(
            self.search_bar_locator)
        search_bar.send_keys(f"{song['title']} - {song['artist']}")
        search_bar.send_keys(Keys.ENTER)

    def add_song(self, song):
        self.search_for_song(song)
        self.selenium_service.wait_until_element_text_to_be(
            self.first_song_title_locator, song['title'])
        self.selenium_service.wait_until_element_text_to_be(
            self.first_song_artist_locator, song['artist'])
        self.selenium_service.find_element(
            self.first_song_options_locator).click()
        self.selenium_service.hover_over_element(
            self.add_to_playlist_locator)
        self.selenium_service.wait_until_located(
            self.add_to_playlist_btn_locator).click()
