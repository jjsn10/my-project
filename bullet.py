import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """This class handle the bullets shooted from the ship"""
    def __init__(self, ai_configurations, screen, ship):
        super (Bullet, self).__init__()
        self.screen = screen

        #Create a bullet in (0,0) and set the position
        self.rect = pygame.Rect(0,0, ai_configurations.bullet_width, ai_configurations.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_configurations.bullet_color
        self.factor_speed = ai_configurations.bullet_factor_speed

    def update(self):
        """Move the bullet to the top of the screen"""

        #update de decimal position of the bullet
        self.y -= self.factor_speed

        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)




