import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.login_page_service import LoginPage
from ui.pages.main_page_service import MainPage

playlist_name = "Julian's Favs Mashup Playlist"
playlist_songs = [{
    "song": "Baby", 
    "artist": "Justin Bieber"
}]

class TestSpotify:
    def setup(self):
        self.username = "julian.automation.test@gmail.com"
        self.password = "Testing1!"
        self.main_page = MainPage()
        self.login_page = LoginPage()

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://open.spotify.com/")
        driver.maximize_window()
        self.main_page.login(driver)
        self.login_page.login(driver, self.username, self.password)
        time.sleep(5)
    