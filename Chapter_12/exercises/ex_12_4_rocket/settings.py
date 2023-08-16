"""Creating a Setting class for exercise 12-4"""


class Settings:
    """A class to store all settings for Rocket Game."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (178, 190, 181)

        # Rocket settings.
        self.rocket_speed = 1.5
