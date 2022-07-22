class Statistics():
    """Tracking the statistics of Alien Invasion"""
    def __init__(self, ai_configurations):
        """Initiate statistics"""
        self.ai_configurations = ai_configurations
        self.reset_stats()

        #Initiate Alien invation in an active state
        self.game_active = False

        # the highest score should be never restarted
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_remains = self.ai_configurations.ships_number
        self.score = 0
        self.level = 1