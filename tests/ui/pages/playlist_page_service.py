class PlaylistPage:
    def __init__(self):
        self.playlist_name_button_locator = "//span[@data-testid='entityTitle]/button"
        self.playlist_name_text_locator = "//span[@data-testid='entityTitle]/button/span/h1"

    def rename_playlist(self, test_user, playlist_name):
        