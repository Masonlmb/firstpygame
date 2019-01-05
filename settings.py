class Settings():

    '''include all game setting'''

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #setting for ship
        self.ship_speed_factor = 5
        self.ship_limit = 3

        #setting for bullte
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20


        #setting for alien

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #fleet direction

        self.fleet_direction = 1



