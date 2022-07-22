import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Contro  the behave of the ship"""
    def __init__(self, ai_configurations, screen):
        """Initiate the shipt and set the init position of the ship"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_configurations = ai_configurations
        #Load ship image and get the rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value to center the ship
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position according to the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_configurations.speed_ship_factor
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_configurations.speed_ship_factor
        
        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship in the current location"""
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx