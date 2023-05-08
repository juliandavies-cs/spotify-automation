import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.login_page_service import LoginPage
from ui.pages.main_page_service import MainPage
from ui.util.selenium_service import SeleniumService

playlist_name = "Julian's Favs Mashup Playlist"
playlist_songs = [{
    "song": "Baby", 
    "artist": "Justin Bieber"
}]

class TestSpotify:
    def setup_method(self):
        self.username = "julian.automation.test@gmail.com"
        self.password = "Testing1!"
        self.selenium_service = SeleniumService()
        self.main_page = MainPage()
        self.login_page = LoginPage()
        self.test_case = self

    def test_login(self):
        driver = self.selenium_service.openURL("https://open.spotify.com/")
        self.main_page.login(self.test_case)
        self.login_page.login(self.test_case, self.username, self.password)
        time.sleep(5)
    