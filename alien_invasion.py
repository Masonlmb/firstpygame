import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # init game and creat a screen obj
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #creat new stats ob
    stats = GameStats(ai_settings)

    #creat ship
    ship =  Ship(ai_settings, screen)
    #creat bullets group
    bullets = Group()
    #creat alien group
    aliens = Group()

    gf.creat_fleet(ai_settings, screen,ship, aliens)

    #creat play button

    play_button = Button(ai_settings, screen, 'play')


    #start game main loop

    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship,aliens, bullets, play_button)



run_game()

