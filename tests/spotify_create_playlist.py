from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

playlist_name = "Julian's Favs Mashup Playlist"
playlist_songs = [{
    "song": "Baby",
    "artist": "Justin Bieber"
}]

def test_create_playlist():
    driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/")
    driver.maximize_window()
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='login-button']"))
    )
    login_button.click()
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-username"))
    )
    username_input.send_keys("julian.automation.test@gmail.com")
    password_input = driver.find_element(By.ID, "login-password")
    password_input.send_keys("Testing1!")
    login_button_account_page = driver.find_element(By.ID, "login-button")
    login_button_account_page.click()
    time.sleep(5)