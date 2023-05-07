import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.login_page import *

# vars
username = "julian.automation.test@gmail.com"
password = "Testing1!"
playlist_name = "Julian's Favs Mashup Playlist"
playlist_songs = [{
    "song": "Baby", 
    "artist": "Justin Bieber"
}]
    
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/")
    driver.maximize_window()
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='login-button']"))
    )
    login_button.click()
    login(driver, username, password)
    