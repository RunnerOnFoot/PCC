"""Exercise 12-1"""

import sys

import pygame

from settings import Settings


class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, And create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
