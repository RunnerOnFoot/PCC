"""Creating a Settings Class"""


class Settings:
    """A class to store all settings for the game."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (40, 160, 200)
