import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    '''alien class'''

    def __init__(self,ai_settings, screen):
        '''init alien and set first position'''

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        #load alien pic and set its rect

        self.image = pygame.image.load('images/aim.bmp')
        self.rect = self.image.get_rect()


        #ervery new alien at the up-left conner

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #set alien float position

        self.x = float(self.rect.x)

    def blitme(self):
        '''creat new alien at first position'''

        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        '''if going right return 1 if going left returen -1'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True



    def update(self):
        '''move alien to right'''


        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

