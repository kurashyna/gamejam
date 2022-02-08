from asyncio.windows_events import NULL
import random
import pygame

from terrain import Terrain
from terrainelement import *


class Environment:
    def __init__(self, game):
        self.game = game
        self.dayTime = 5000

        self.dayOrNight = "night"
        self.toggleDay()
        self.lastTimeChanged = 0
        self.lastTimeMeteorStartedFalling = 0
        self.lastTimeMeteorFalled = 0
        self.delayBeforeFalling = 500
        self.meteorShadow = NULL

    def update(self):
        currentTime = pygame.time.get_ticks()
        # change day and night
        if currentTime > self.lastTimeChanged + self.dayTime:
            self.lastTimeChanged = pygame.time.get_ticks()
            self.toggleDay()
        # make meteors fall

        # le meteor a commencé mais n'a pas fini de tomber
        if self.lastTimeMeteorStartedFalling > self.lastTimeMeteorFalled:
            if currentTime > self.lastTimeMeteorStartedFalling + self.delayBeforeFalling:
                self.fallMeteor()
                self.lastTimeMeteorFalled = currentTime
        elif self.dayOrNight == "night":
            # no meteor is currently falling
            if currentTime > self.lastTimeMeteorStartedFalling + 2000:
                self.lastTimeMeteorStartedFalling = currentTime
                self.appearMeteor()

    def toggleDay(self):
        if self.dayOrNight == "day":
            self.music = pygame.mixer.music.load(
                "assets/sounds/music/night.mp3")
            pygame.mixer.music.play(-1)  # change the music
            self.dayOrNight = "night"
        else:
            self.music = pygame.mixer.music.load("assets/sounds/music/day.mp3")
            pygame.mixer.music.play(-1)  # change the music
            self.dayOrNight = "day"
            pygame.mixer.music.play(0)
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
