import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        '''creat a bullet ob at ship position'''

        super().__init__()
        self.screen = screen

        #creat a bullet at (0,0) and the put it correct place

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #use float number as bullet position

        self.y = float(self.rect.y)


        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor



    def update(self):
            '''move bullet up'''

            #renew self.y

            self.y -= self.speed_factor

            #renew rect.y

            self.rect.y = self.y

    def draw_bullet(self):
            '''draw bullet on screen'''

            pygame.draw.rect(self.screen, self.color, self.rect)

