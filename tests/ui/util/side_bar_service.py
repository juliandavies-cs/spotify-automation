from ui.util.selenium_service import SeleniumService


class SideBar:
    def __init__(self):
        self.selenium_service = SeleniumService()

        self.playlist_text_sidebar_locator = \
            "//p[contains(@id, 'listrow-title-spotify:playlist')]/span"
        self.playlist_btn_locator = \
            "//p[contains(@id, 'listrow-title-spotify:playlist')]" + \
            "/../../../button"
        self.search_btn = "//a[@href='/search']"

    def click_search(self):
        self.selenium_service.find_element(self.search_btn).click()

    def click_playlist(self):
        self.selenium_service.wait_until_element_text_to_be(
            self.playlist_text_sidebar_locator, "My Playlist #1")
        self.selenium_service.find_element(self.playlist_btn_locator).click()

    def verify_playlist_created(self):
        self.selenium_service.wait_until_element_text_to_be(
            self.playlist_text_sidebar_locator, "My Playlist #1")
        return True
