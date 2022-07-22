import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """This class is used to represent a one Alien"""
    def __init__(self, ai_configurations, screen):
        """Initialize alien and set its initial position"""
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_configurations = ai_configurations

        # Load the alien image and set up its rec attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Initialize each new alien close to the left top part of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the exact position of the alien 
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien in its current location"""
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        """Return True if the alien is close to the screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Move alien to the right side"""
        self.x += (self.ai_configurations.alien_speed_factor * self.ai_configurations.fleet_direction)
        self.rect.x = self.x



