import pygame
from abc import ABC


class TerrainElement(ABC):  # abstract class
    def __init__(self, x, y, scale, image):
        # made with a method so that it can be set in each class
        self.image = pygame.image.load(image)
        self.setScale(scale)  # change the size of the object
        self.rect = self.image.get_rect(x=x, y=y)

    def move(self, xDirection, yDirection):
        self.rect.move_ip(xDirection, yDirection)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # virtual methods
    def setScale(self, scale):
        self.size = self.image.get_size()  # obtient la taille de l'image
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0]*scale), int(self.size[1]*scale)))  # multiplie la taille de x et y par 5

    def update(self, player):
        pass


class Obstacle(TerrainElement):
    def __init__(self, x, y, scale):
        imageLocation = "assets/sprites/png/background/moulin.png"
        TerrainElement.__init__(self, x, y, scale, imageLocation)

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.bounce()


class Fruit(TerrainElement):
    def __init__(self, terrain, x, y, scale):
        self.terrain = terrain
        imageLocation = "assets/sprites/png/fruits/pear.png"
        TerrainElement.__init__(self, x, y, scale, imageLocation)

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.addDash()
            self.getEaten()

    def getEaten(self):
        self.terrain.fruits.remove(self)


class Ground(TerrainElement):
    def __init__(self, x, y):
        scale = 5
        imageLocation = "assets/sprites/png/background/terrain.png"
        TerrainElement.__init__(self, x, y, scale, imageLocation)
