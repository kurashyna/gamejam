from fileinput import filename
import pygame
from abc import ABC
import random


class TerrainElement(ABC):  # abstract class

    def __init__(self, x, y, scale, folder, filename):
        # made with a method so that it can be set in each class
        self.folder = folder
        self.filename = filename
        # self.image = pygame.image.load(self.folder + self.filename)
        self.scale = scale
        self.toggleSprite(self.nightOrDay())

        # self.setScale(self.scale)  # change the size of the object
        self.rect = self.image.get_rect(x=x, y=y)
        self.freeze=False

    def nightOrDay(self):
        return "night"  # asteroids and lazers always fall at night so it defaults to night

    def move(self, xDirection, yDirection):
        self.rect.move_ip(xDirection, yDirection)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # virtual methods
    def setScale(self):
        self.size = self.image.get_size()  # obtient la taille de l'image
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0]*self.scale), int(self.size[1]*self.scale)))  # multiplie la taille de x et y par 5

    def toggleSprite(self, dayOrNight):
        # made with a method so that it can be set in each class
        self.setSprite(dayOrNight)
        self.setScale()

    def setSprite(self, dayOrNight):
        self.image = pygame.image.load(
            self.folder + dayOrNight + "/" + self.filename + ".png")

    def update(self, player):
        pass


class Obstacle(TerrainElement):
    def __init__(self, terrain, x, y, scale, type):
        self.type = type
        folder = "assets/sprites/png/terrain/obstacles/"
        filename = self.type
        TerrainElement.__init__(self, x, y, scale, folder, filename)
        if self.type == "meteor":
            terrain.effects.append(Smoke(terrain, x - 60, y - 80))

    def update(self, player):
        if self.freeze == False :
            if self.rect.colliderect(player.rect):
                player.bounce()


class Fruit(TerrainElement):
    def __init__(self, terrain, x, y, scale, dayOrNight):
        self.dayOrNight = dayOrNight
        self.randomfruit = random.randrange(0, 4)
        self.terrain = terrain
        folder = "assets/sprites/png/terrain/fruits/"
        if self.randomfruit == 0:
            filename = "pear"
        elif self.randomfruit == 1:
            filename = "apple"
        elif self.randomfruit == 2:
            filename = "cherry"
        elif self.randomfruit == 3:
            filename = "banana"

        TerrainElement.__init__(self, x, y, scale, folder, filename)

    def nightOrDay(self):
        return self.dayOrNight

    def update(self, player):
        if self.rect.colliderect(player.rect):

            if self.randomfruit == 0:
                player.addDash()
                scoreAmount = 2
            elif self.randomfruit == 1:
                player.mouvementspeedbuff()
                scoreAmount = 4
            elif self.randomfruit == 2:
                player.recoveryhp()
                scoreAmount = 2
            elif self.randomfruit == 3:
                player.addFreezeall()
                scoreAmount = 2
            player.addScore(scoreAmount)
            self.getEaten()

    def getEaten(self):
        self.terrain.fruits.remove(self)


class Ground(TerrainElement):
    def __init__(self, x, y):
        scale = 5
        folder = "assets/sprites/png/terrain/background/"
        filename = "ground"
        TerrainElement.__init__(self, x, y, scale, folder, filename)

    def update(self, player):
        if not self.rect.colliderect(player.rect):
            player.bounce()


class Smoke(TerrainElement):
    def __init__(self, terrain, x, y):
        self.terrain = terrain
        scale = 7
        folder = "assets/sprites/png/smoke_animation/"
        self.lastTimeFrameChanged = 0
        self.currentFrame = 0
        filename = "smoke_" + str(self.currentFrame)
        TerrainElement.__init__(self, x, y, scale, folder, filename)

    def update(self, player):
        if pygame.time.get_ticks() > self.lastTimeFrameChanged + 83:
            if self.currentFrame == 5:
                self.terrain.effects.remove(self)
            else:
                self.currentFrame += 1

            self.lastTimeFrameChanged = pygame.time.get_ticks()
            self.filename = "smoke_" + str(self.currentFrame)
            self.toggleSprite("day")


class MeteorShadow(TerrainElement):
    def __init__(self, x, y):
        scale = random.randrange(7, 15)
        folder = "assets/sprites/png/smoke_animation/"

        self.lastTimeFrameChanged = 0
        self.currentFrame = 0
        # filename = "smoke_" + str(self.currentFrame)
        filename = "meteor_shadow"
        TerrainElement.__init__(self, x, y, scale, folder, filename)


class Projectile(TerrainElement):
    def __init__(self, game, creationTime, minSpeed):
        self.game = game
        self.creationTime = creationTime
        self.expirationDate = 10000
        x = random.randrange(-800, -400)
        y = random.randrange(-400, game.screen.get_size()[1]+200)
        self.velocity = random.randrange(minSpeed, minSpeed + 4)
        scale = 2
        folder = "assets/sprites/png/terrain/projectiles/"
        filename = "laser"
        TerrainElement.__init__(self, x, y, scale, folder, filename)

    def update(self, player):
        if self.freeze == False :
            self.rect.move_ip(self.velocity, 0)
            if self.rect.colliderect(player.rect):
                player.loseHP()
                # projectile deletes itself when it touches character
                self.delete()
            if pygame.time.get_ticks() > self.creationTime + self.expirationDate:
                self.delete()
        else :
            currentTime = pygame.time.get_ticks()
            print(pygame.time.get_ticks())
            if currentTime > 15000 :
                self.freeze = False
    def delete(self):
        self.game.terrain.projectiles.remove(self)
