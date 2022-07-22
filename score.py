import pygame.font
from pygame.sprite import Group

from ship import Ship

class Score():
    """It is a class to report information about score"""
    def __init__(self, ai_configurations, screen, statistics):
        """Initialize score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_configurations = ai_configurations
        self.statistics = statistics

        #Font settings to show score
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def  prep_score(self):
        """Convert the score to be a rendered image"""
        score_rounded = int(round(self.statistics.score, -1))
        score_str = "{:,}".format(score_rounded)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_configurations.bg_color)

        #Show the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Convert the score to be a rendered image"""
        high_point = int(round(self.statistics.high_score, -1))
        high_score_str = "{:,}".format(high_point)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_configurations.bg_color)

        #Center the high score at the top center of the screen
        self.high_point_rect = self.high_score_image.get_rect()
        self.high_point_rect.centerx = self.screen_rect.centerx
        self.high_point_rect.top = self.score_rect.top

    def prep_level(self):
        """Convert the level in a rendered image"""
        self.image_level = self.font.render(str(self.statistics.level), True, self.text_color, self.ai_configurations.bg_color)

        #Put the level under score on the screen
        self.level_rect = self.image_level.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships left we have"""
        self.ships = Group()
        for ship_number in range (self.statistics.ships_remains):
            ship = Ship(self.ai_configurations, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def  show_score(self):
        """draw the score at the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_point_rect)
        self.screen.blit(self.image_level, self.level_rect)

        #Draw the ships
        self.ships.draw(self.screen)
