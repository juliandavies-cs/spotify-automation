import time
import pytest

from ui.pages.login_page_service import LoginPage
from ui.pages.main_page_service import MainPage
from ui.pages.playlist_page_service import PlaylistPage
from ui.util.side_bar_service import SideBar
from ui.util.selenium_service import SeleniumService

class TestSpotify:
    def setup_method(self):
        self.test_case = self
        self.email = "julian.automation.test@gmail.com"
        self.password = "Testing1!"
        self.username = "Automation-Test"
        self.url = "https://open.spotify.com/"
        self.selenium_service = SeleniumService()
        self.main_page = MainPage()
        self.login_page = LoginPage()
        self.playlist_page = PlaylistPage()
        self.side_bar_service = SideBar()

    def test_login(self):
        """ Verify user can login """
        self.selenium_service.open_url(self.url)
        self.main_page.login(self.test_case)
        self.login_page.login(self.test_case, self.email, self.password)
        self.main_page.verify_successful_login(self.test_case, self.username)
        self.selenium_service.close()

    @pytest.mark.slow
    def test_create_playlist(self):
        """ Verify a playlist can be creating given some songs """
        playlist_songs = [
            {
            "title": "Alive", 
            "artist": "The Scarlet Opera"
            },
            {
            "title": "I Don't Wanna Know", 
            "artist": "Knox"
            },
            {
            "title": "Joe", 
            "artist": "Luke Combs"
            }
        ]

        self.selenium_service.open_url(self.url)
        self.main_page.login(self.test_case)
        self.login_page.login(self.test_case, self.email, self.password)
        self.main_page.create_playlist(self.test_case)
        self.side_bar_service.verify_playlist_created(self.test_case)

        for song in playlist_songs:
            self.main_page.add_song(self.test_case, song)
        
        self.side_bar_service.click_playlist(self.test_case)
        self.playlist_page.verify_songs_added(self.test_case, playlist_songs)

        time.sleep(5)

        # cleanup
        self.playlist_page.delete_playlist(self.test_case)

    