from pygame.sprite import Sprite


class enemy(Sprite):
    def __init__(self, enemy_tank, name, screen):
        super(enemy, self).__init__()
        self.enemy_tank = enemy_tank
        self.name = name
        self.screen = screen
        self.speed_factor = alien_settings.x_speed
