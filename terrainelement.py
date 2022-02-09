from fileinput import filename
import pygame
from abc import ABC


class TerrainElement(ABC):  # abstract class
    def __init__(self, x, y, scale, folder, filename):
        # made with a method so that it can be set in each class
        self.folder = folder
        self.filename = filename
        # self.image = pygame.image.load(self.folder + self.filename)
        self.scale = scale
        self.toggleSprite("night")
        # self.setScale(self.scale)  # change the size of the object
        self.rect = self.image.get_rect(x=x, y=y)

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
        if self.rect.colliderect(player.rect):
            player.bounce()


class Fruit(TerrainElement):
    def __init__(self, terrain, x, y, scale):
        self.terrain = terrain
        folder = "assets/sprites/png/terrain/fruits/"
        filename = "pear"
        TerrainElement.__init__(self, x, y, scale, folder, filename)

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.addDash()
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
                self.currentFrame = 0
                self.terrain.effects.remove(self)
            else:
                self.currentFrame += 1

            self.lastTimeFrameChanged = pygame.time.get_ticks()
            self.filename = "smoke_" + str(self.currentFrame)
            self.toggleSprite("day")


class MeteorShadow(TerrainElement):
    def __init__(self, x, y):
        scale = 7
        folder = "assets/sprites/png/smoke_animation/"

        self.lastTimeFrameChanged = 0
        self.currentFrame = 0
        # filename = "smoke_" + str(self.currentFrame)
        filename = "meteor_shadow"
        TerrainElement.__init__(self, x, y, scale, folder, filename)


class Projectile(TerrainElement):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.velocity = 8

    def draw(self, screen):
        self.line = pygame.draw.line(screen, self.color, (self.x, self.y),
                                     (self.x + 100, self.y))
        screen.blit(screen, self.line)
