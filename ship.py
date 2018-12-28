import pygame

class Ship():


    def __init__(self, ai_settings, screen):
        '''init ship and first position'''

        self.screen = screen
        self.ai_settings = ai_settings
        #load ship image
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put new ship at the middle of bottom

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''moving ship depens on self.moving_right'''

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):

        '''creat ship'''

        self.screen.blit(self.image,self.rect)


