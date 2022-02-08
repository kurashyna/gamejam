from asyncio.windows_events import NULL
import random
import pygame

from terrain import Terrain
from terrainelement import *


class Environment:
    def __init__(self, game):
        self.game = game
        self.dayTime = 5000
        self.dayOrNight = "day"
        self.lastTimeChanged = 0
        self.lastTimeMeteorStartedFalling = 0
        self.lastTimeMeteorFalled = 0
        self.delayBeforeFalling = 200
        self.meteorShadow = NULL

    def update(self):
        currentTime = pygame.time.get_ticks()
        # change day and night
        if currentTime > self.lastTimeChanged + self.dayTime:
            self.lastTimeChanged = pygame.time.get_ticks()
            self.toggleDay(self.dayOrNight)
        # make meteors fall

        # le meteor a commencé mais n'a pas fini de tomber
        if self.lastTimeMeteorStartedFalling > self.lastTimeMeteorFalled:
            if currentTime > self.lastTimeMeteorStartedFalling + self.delayBeforeFalling:
                self.fallMeteor()
                self.lastTimeMeteorFalled = currentTime
        elif currentTime > self.lastTimeMeteorStartedFalling + 2000:
            self.lastTimeMeteorStartedFalling = currentTime
            self.appearMeteor()

    def toggleDay(self, isDay):
        if self.dayOrNight == "day":
            self.dayOrNight = "night"
        else:
            self.dayOrNight = "day"
        self.game.terrain.setSprites(self.dayOrNight)
        print(self.dayOrNight)

    def appearMeteor(self):
        self.meteorShadow = MeteorShadow(random.randrange(self.game.player.rect.x - 200, self.game.player.rect.x + 200),
                                         random.randrange(self.game.player.rect.y - 200, self.game.player.rect.y + 200))
        self.game.terrain.effects.append(self.meteorShadow)

    def fallMeteor(self):
        self.game.terrain.obstacles.append(
            Obstacle(self.game.terrain, self.meteorShadow.rect.x, self.meteorShadow.rect.y, 7, "meteor"))
        self.game.terrain.effects.remove(self.meteorShadow)

        print("je suis tombé")
