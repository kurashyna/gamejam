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
        self.delayBetweenMeteor = 2000
        self.fruit = NULL
        self.lastTimeFruitAppear = 0
        self.groundrect=(self.game.terrain.ground.rect)

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
                if self.delayBeforeFalling > 100:
                    self.delayBeforeFalling = self.delayBeforeFalling-10

                if self.delayBetweenMeteor > 500 :
                    self.delayBetweenMeteor = self.delayBetweenMeteor-20

        elif self.dayOrNight == "night":
            # no meteor is currently falling
            if currentTime > self.lastTimeMeteorStartedFalling + self.delayBetweenMeteor :
                self.lastTimeMeteorStartedFalling = currentTime
                self.appearMeteor()

        if currentTime > self.lastTimeFruitAppear + 5000 :
            self.lastTimeFruitAppear = currentTime
            self.appearFruit()

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

    def appearFruit(self):
        self.game.terrain.fruits.append(Fruit(self.game.terrain ,random.randrange(self.groundrect.left,self.groundrect.right),random.randrange(self.groundrect.top,self.groundrect.bottom),1))
    def fallMeteor(self):
        self.game.terrain.obstacles.append(
            Obstacle(self.game.terrain, self.meteorShadow.rect.x, self.meteorShadow.rect.y, 7, "meteor"))
        self.game.terrain.effects.remove(self.meteorShadow)
