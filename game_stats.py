class GameStats():

    '''record game stats'''

    def __init__(self, ai_settings):
        #init stats information
        self.ai_settings = ai_settings
        self.reset_stats()

        # set game unactive at begining
        
        self.game_active = False



    def reset_stats(self):
        '''init all information'''

        self.ships_left = self.ai_settings.ship_limit
