"""Creating the Bird Class"""

import pygame


class Bird:
    """A class to manage the bird."""

    def __init__(self, bbg_game) -> None:
        """Initialize the bird and set it's starting position."""
        self.screen = bbg_game.screen
        self.screen_rect = bbg_game.screen.get_rect()

        # Load the bird image and get it's rect.
        self.image = pygame.image.load(
            r'Chapter_12\exercises\ex_12_2_game_character\images\bird_small.bmp')
        self.rect = self.image.get_rect()

        # Start each new bird at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it's current location."""
        # screen.blit() : doesn't update screen - it draws image in buffer.
        self.screen.blit(self.image, self.rect)
