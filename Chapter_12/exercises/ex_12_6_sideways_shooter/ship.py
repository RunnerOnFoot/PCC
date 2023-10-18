"""Creating a ship class for sideways_shooter.py"""

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ss_game) -> None:
        """Initialize the ship and set it's starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load(
            r'Chapter_12\exercises\ex_12_6_sideways_shooter\images\rocket_small.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the center of the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
