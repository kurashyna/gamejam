import pygame
# from fruit import Fruit
# from obstacle import Obstacle
# to be able to use abstract methods
from abc import ABC, abstractmethod


class Terrain:
    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.image = pygame.image.load(
            "assets/sprites/png/background/terrain.png")
        self.rect = self.image.get_rect()
        self.obstacles = [Obstacle(800, 300, 5), Obstacle(200, 300, 3)]
        self.fruits = [Fruit(self, 700, 200, 1),
                       Fruit(self, 300, 200, 2)]

    def move(self, xDirection, yDirection):
        self.rect.move_ip(xDirection, yDirection)
        for obstacle in self.obstacles:
            obstacle.move(xDirection, yDirection)
        for fruit in self.fruits:
            fruit.move(xDirection, yDirection)

    def update(self, player):
        # detecte les collisions avec le joueur
        for obstacle in self.obstacles:
            obstacle.update(player)
        for fruit in self.fruits:
            fruit.update(self.player)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for fruit in self.fruits:
            fruit.draw(screen)


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

    def setImage(self):
        pass

    def update(self, player):
        pass


class Obstacle(TerrainElement):
    def __init__(self, x, y, scale):
        imageLocation = "assets/sprites/png/background/moulin.png"
        TerrainElement.__init__(self, x, y, scale, imageLocation)

    def setImage(self):
        return pygame.image.load("assets/sprites/png/background/moulin.png")

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.bounce()


class Fruit(TerrainElement):
    def __init__(self, terrain, x, y, scale):
        self.terrain = terrain
        imageLocation = "assets/sprites/png/fruits/pear.png"
        TerrainElement.__init__(self, x, y, scale, imageLocation)

    def setImage(self):
        return pygame.image.load("assets/sprites/png/fruits/pear.png")

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.addDash()
            self.getEaten()

    def getEaten(self):
        self.terrain.fruits.remove(self)
