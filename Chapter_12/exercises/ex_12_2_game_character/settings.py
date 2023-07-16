"""
Settings for Blue Bird Game
Exercise 12-2
"""

import pygame


class Settings:
    """A class to store all settings for Blue Bird Game."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 780
        self.bg_color = (0, 0, 0)
