import pygame

from terrain import Terrain


class Environment:
    def __init__(self, game):
        self.game = game
        self.dayTime = 5000
        self.dayOrNight = "day"
        self.lastTimeChanged = 0

    def update(self):
        if pygame.time.get_ticks() > self.lastTimeChanged + self.dayTime:
            self.lastTimeChanged = pygame.time.get_ticks()
            self.toggleDay(self.dayOrNight)

    def toggleDay(self, isDay):
        if self.dayOrNight == "day":
            self.dayOrNight = "night"
        else:
            self.dayOrNight = "day"
        self.game.terrain.setSprites(self.dayOrNight)
        print(self.dayOrNight)
