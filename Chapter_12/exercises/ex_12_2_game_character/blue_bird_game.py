"""Exercise 12-2"""
import sys

import pygame

from settings import Settings
from bird import Bird


class BlueBirdGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Bird Game")

        self.bird = Bird(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.bird.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    bbg = BlueBirdGame()
    bbg.run_game()
