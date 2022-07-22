import statistics
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_configurations, screen, ship, bullets):
    """Respond to the press keys"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        bullet_fire(ai_configurations, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_configurations, screen, statistics, score, play_button, ship, aliens, bullets):
    """reponse to the keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_configurations, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_configurations, screen, statistics, score, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_configurations, screen, statistics, score, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player click on play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not statistics.game_active:
        # Restart game configuration
        ai_configurations.initialize_dynamic_configurations()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)
        #Restart the statistics of the game
        statistics.reset_stats()
        statistics.game_active = True

        #Restart score images
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_configurations, screen, ship, aliens)
        ship.center_ship()

            


def update_screen(ai_configurations, screen, statistics, score, ship, aliens, bullets, play_button):
    """Update the images on the screen and pass the new screen"""

    # drawing the screen in each loop iteration
    screen.fill(ai_configurations.bg_color)
    # Draw again all bullets behind the ship and the alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Draw information about score
    score.show_score()
    #Draw play button if the game is inactive
    if not statistics.game_active:
        play_button.draw_button()


    # Make visible the most recent screen draw
    pygame.display.flip()

def update_balas(ai_configurations, screen, statistics, score, ship, aliens, bullets):
    """Update the bullet position and delete the old one"""

    bullets.update()
    #update the bullet position
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets)) 

    check_bullet_alien_collision(ai_configurations, screen, statistics, score, ship, aliens, bullets)
    
def check_bullet_alien_collision(ai_configurations, screen, statistics, score, ship, aliens, bullets):
    """Responds to the collision between bullets and aliens"""
    # Delete bullets and Aliens that have been hit
    collisions = pygame.sprite.groupcollide(bullets,aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            statistics.score += ai_configurations.alien_points * len(aliens)
            score.prep_score()
        
        check_high_score(statistics, score)


    if len(aliens) == 0:
        #destroy the existing bullet and create a new fleet
        bullets.empty()
        ai_configurations.increase_speed()

        #Increase the level
        statistics.level += 1
        score.prep_level()

        create_fleet(ai_configurations, screen, ship, aliens)

def check_high_score(statistics, score):
    """verify if it exists a high score"""
    if statistics.score > statistics.high_score:
        statistics.high_score = statistics.score
        score.prep_high_score()

def bullet_fire(ai_configurations, screen, ship, bullets):
    """Shoot a bullet if the limit hasn't been reached"""
    #Create a new Bullet and add it to Bullet group
    if len(bullets) < ai_configurations.bullets_allowed:
        new_bullet = Bullet(ai_configurations, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_configurations, alien_width):
    """Determine the number of Aliens that fit in a row"""
    available_space_x = ai_configurations.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/ (2 * alien_width))

    return number_aliens_x

def get_number_rows(ai_configurations, ship_height, alien_height):
    """Determine the number of rows of aliens that fit in the screen"""
    available_space_y = (ai_configurations.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def create_alien(ai_configurations, screen, aliens,alien_number, row_number):
    """Create an alien and put it to the row"""
    alien = Alien(ai_configurations, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_configurations, screen, ship, aliens):
    """Create a complete fleet of aliens"""
    #Create an Alien and find the number of aliens
    #The espace between each alien is equal to the width of alien
    alien = Alien(ai_configurations, screen)
    number_aliens_x = get_number_aliens_x(ai_configurations,alien.rect.width)
    number_rows = get_number_rows(ai_configurations, ship.rect.height, alien.rect.height)


    #Create the flee of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_configurations, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_configurations, aliens):
    """Respond if an alien reached a edge of the screen """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_configurations, aliens)
            break
def change_fleet_direction(ai_configurations, aliens):
    """All fleet Going Down and change the fleet's directions"""
    for alien in aliens.sprites():
        alien.rect.y += ai_configurations.fleet_drop_speed
    ai_configurations.fleet_direction *= -1 

def ship_hitted(ai_configurations, statistics, screen, score, ship, aliens, bullets):
    """Respond if a ship is hitted by a alien"""
    
    if statistics.ships_remains > 0:
        #decrease remained ships
        statistics.ships_remains -= 1

        #Update the score
        score.prep_ships()

        #empty the alien and bullet list
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_configurations, screen, ship, aliens)
        ship.center_ship()

        #Pause
        sleep(0.5)
    else:
        statistics.game_active = False
        pygame.mouse.set_visible(True)
    

def check_aliens_bottom(ai_configurations, statistics, screen, score, ship, aliens, bullets):
    """Check if any alien has been reachead to the end of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #behave as the same way as the ship was hitten
            ship_hitted(ai_configurations, statistics, screen, score, ship, aliens, bullets)
            break

def update_aliens(ai_configurations, statistics, screen, score, ship, aliens, bullets):
    """Check if the fleet is to the edge and then update the alien's positions"""
    check_fleet_edges(ai_configurations, aliens)
    aliens.update()

    #Find collisions of Alien-Ship
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("!Ship hitted!")
        ship_hitted(ai_configurations, statistics, screen, score, ship, aliens, bullets)

    #find alien that hit the bottom part of the screen
    check_aliens_bottom(ai_configurations, statistics, screen, score, ship, aliens, bullets)

