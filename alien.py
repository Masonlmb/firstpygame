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

        self.image = pygame.image.load('images/aim.png')
        self.rect = self.image.get_rect()


        #ervery new alien at the up-left conner

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #set alien float position

        self.x = float(self.rect.x)

    def blitme(self):
        '''creat new alien at first position'''

        self.screen.blit(self.image, self.rect)


