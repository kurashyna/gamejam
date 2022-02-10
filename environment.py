from asyncio.windows_events import NULL
import random
from turtle import screensize
import pygame

from terrain import Terrain
from terrainelement import *


class Environment:
    def __init__(self, game):
        self.game = game
        self.dayTime = 5000
        self.dayOrNight = "night"
        self.toggleDay()
        self.lastTimeChanged = pygame.time.get_ticks()
        self.lastTimeMeteorStartedFalling = 0
        self.lastTimeMeteorFalled = 0
        self.delayBeforeFalling = 600
        self.meteorShadow = NULL
        self.delayBetweenMeteor = 2000
        self.lastTimeFruitAppear = 0
        self.groundrect = (self.game.terrain.ground.rect)
        self.lastTimeLazerWasShot = 0
        self.lazerSpawnDelay = 200

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

                if self.delayBetweenMeteor > 500:
                    self.delayBetweenMeteor = self.delayBetweenMeteor-20

        elif self.dayOrNight == "night":
            # no meteor is currently falling
            if currentTime > self.lastTimeMeteorStartedFalling + self.delayBetweenMeteor:
                self.lastTimeMeteorStartedFalling = currentTime
                self.appearMeteor()
        if self.dayOrNight == "day":
            if currentTime > self.lastTimeFruitAppear + 1000:
                self.lastTimeFruitAppear = currentTime
                self.appearFruit()

        # lazers
        for lazer in self.game.terrain.projectiles:
            lazer.update(self.game.player)
        if self.dayOrNight == "night" and currentTime > self.lastTimeLazerWasShot + self.lazerSpawnDelay:
            self.game.terrain.projectiles.append(
                Projectile(self.game, currentTime))
            self.lastTimeLazerWasShot = currentTime

    def toggleDay(self):
        if self.dayOrNight == "day":
            # change to night
            self.music = pygame.mixer.music.load(
                "assets/sounds/music/night.mp3")
            pygame.mixer.music.play(-1)  # change the music
            self.dayOrNight = "night"
            self.game.hud.score.addValue(
                self.game.hud.score.value)  # doubles the score
        else:
            # change to day
            self.music = pygame.mixer.music.load("assets/sounds/music/day.mp3")
            pygame.mixer.music.play(-1)  # change the music
            self.dayOrNight = "day"
            pygame.mixer.music.play(0)
        self.game.terrain.setSprites(self.dayOrNight)

    def fruitIsColliding(self, fruit):
        for obstacle in self.game.terrain.obstacles:
            if obstacle.rect.colliderect(fruit.rect):
                return True
        return False

    def appearMeteor(self):
        self.meteorShadow = MeteorShadow(random.randrange(self.game.player.rect.x - 200, self.game.player.rect.x + 200),
                                         random.randrange(self.game.player.rect.y - 200, self.game.player.rect.y + 200))
        self.game.terrain.effects.append(self.meteorShadow)

    def appearFruit(self):
        while True:
            newFruit = Fruit(self.game.terrain, random.randrange(
                self.groundrect.left, self.groundrect.right), random.randrange(self.groundrect.top, self.groundrect.bottom), 1, random.randrange(0, 2))
            if not self.fruitIsColliding(newFruit):
                break
        self.game.terrain.fruits.append(newFruit)

    def fallMeteor(self):
        meteor = Obstacle(self.game.terrain, self.meteorShadow.rect.x,
                          self.meteorShadow.rect.y, random.randrange(7, 15), "meteor")
        self.game.terrain.obstacles.append(meteor)
        self.game.terrain.effects.remove(self.meteorShadow)
        # kill if player under it
        if meteor.rect.colliderect(self.game.player.rect):
            self.game.gameOver()
