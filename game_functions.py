import sys
from time import sleep
from Bullet import Bullet
import pygame
from alien import Alien



def check_keydown_events(event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # ship move right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets):
    '''response for keyboard and mouse action'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)





def fire_bullet(ai_settings, screen, ship, bullets):
    # creat new bullet and added in bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    """update screen"""

    screen.fill(ai_setting.bg_color)

    ship.blitme()
    aliens.draw(screen)

    for bullet in bullets:
        bullet.draw_bullet()

    pygame.display.flip()




def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''update bullet position and number and delete outside bullet'''


    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):

    #check if bullets shoot some alien if so ,delete alien

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) ==0:
        #delete all bullets and creat new fleets
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)




def get_numbe_aliens_x(ai_settings, alien_width):
    '''calculate how many alien in a row'''

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''calculate how many rows alien'''

    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y /(2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''creat a alien and put it in the row'''

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def creat_fleet(ai_settings, screen, ship, aliens):
    '''creat alien fleet'''

    #creat one alien and calculate how many aliens a row
    #distance between aliens is aliens_wide
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_numbe_aliens_x(ai_settings, alien.rect.x)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)



    #creat first row of aliens
    for row_number in range(5):  # 5 should be number_rows
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number,row_number)




def check_fleet_edges(ai_settings, aliens):
    '''change direction when some alien touch boundary'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''move all aliens down and change direcetion'''

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1



def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''when aliens hit ship'''
    if stats.ships_left >0:

        # ship_left -=1
        stats.ships_left -= 1

        #clear aliens and bullets
        aliens.empty()
        bullets.empty()

        #creat new fleets put ship in the middle of screen
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause 0.5 sec
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''check if alien touch bottom'''

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship,  aliens, bullets):
    '''update alien fleet position'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #check if any aliens touch ship

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)



