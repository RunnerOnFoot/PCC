"""Creating a setting class"""

import pygame


class Settings:
    """A class to store all settings for Blue Sky."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 160, 200)
