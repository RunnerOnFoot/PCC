"""Exercise 12-1"""

import sys

import pygame


class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, And create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (135, 206, 235)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
