import pygame
from pygame.sprite import Group
from configuration import Configurations
from statistics import Statistics
from score import Score
from ship import Ship
from button import Button
#from alien import Alien
import game_functions as gf


def run_game():
    #Init the game, the configurations and create an screen object
    pygame.init()
    ai_configurations = Configurations()
    screen = pygame.display.set_mode((ai_configurations.screen_width,ai_configurations.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create the button Play
    play_button = Button(ai_configurations, screen, "Play")

    #Create an instance to store statistics of the game and create a score
    statistics = Statistics(ai_configurations)
    score = Score(ai_configurations, screen, statistics)


    # Create a ship
    ship = Ship(ai_configurations, screen)

    #Create a group to store the bullets
    bullets = Group()

    #Create a group of Aliens
    aliens = Group()

    #Create a fleet of aliens
    gf.create_fleet(ai_configurations, screen, ship, aliens)

    #Create an Alien
    #alien = Alien(ai_configurations, screen)



    #Setting background color
    #bg_color = (230,230,230)

    #Init the main loop game
    while True:

        #Listen keyboard and mouse events
        gf.check_events(ai_configurations, screen, statistics, score, play_button, ship, aliens, bullets)
        if statistics.game_active:
            ship.update()
            gf.update_balas(ai_configurations, screen, statistics, score, ship, aliens, bullets)
            gf.update_aliens(ai_configurations, statistics, screen, score, ship, aliens, bullets)

        gf.update_screen(ai_configurations, screen, statistics, score, ship, aliens, bullets, play_button)
    

run_game()