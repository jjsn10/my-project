class Configurations():
    
    def __init__(self):

        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (230,230,230)

        # Ship configurations
        #self.speed_ship_factor = 1.5
        self.ships_number = 3

        #Bullet config
        #self.bullet_factor_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Alien Configurations
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #Doing the game fast
        self.aceleration_scale = 1.1

        #how fast increase the points per alien
        self.scale_score = 1.5

        self.initialize_dynamic_configurations()


        ##fleet_direction, if it 1 represent the right; if it is -1 represent the left
        #self.fleet_direction = 1

    def initialize_dynamic_configurations(self):
        """Initialize configuration changes during the game"""
        self.speed_ship_factor = 1.5
        self.bullet_factor_speed = 3
        self.alien_speed_factor = 1

        #fleet_direction, if it 1 represent the right; if it is -1 represent the left
        self.fleet_direction = 1

        #Alien Points
        self.alien_points = 50
    

    def increase_speed(self):
        """Increase the configuration speed and point values for aliens"""
        self.speed_ship_factor *= self.aceleration_scale
        self.bullet_factor_speed *= self.aceleration_scale
        self.alien_speed_factor *= self.aceleration_scale

        self.alien_points = int(self.alien_points * self.scale_score)

        #checking the points increase
        #print(self.alien_points)





