import pygame
from terrainelement import *
import random

class Terrain:
    def __init__(self, game, player):
        self.player = player
        self.ground = Ground(0, 0)
        self.effects = []
        self.projectile = Projectile(100, 300)
        self.obstacles = [
            Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill"),Obstacle(self,random.randrange(0, 4400),random.randrange(0, 2800), 5, "mill") ]
        self.fruits = [Fruit(self, 700, 200, 1,0), Fruit(self, 300, 200, 1,0),Fruit(self, 350, 220, 1,0),Fruit(self, 400, 200, 1,1),Fruit(self, 800, 200, 1,1),Fruit(self, 1000, 200, 1,1)]
        self.terrainElements = [self.ground,
                                self.obstacles, self.effects, self.fruits, self.projectile]

    def move(self, xDirection, yDirection):
        for terrainElementList in self.terrainElements:  # iterate through all the terrainelements
            if hasattr(terrainElementList, '__iter__'):  # if its iterable
                for terrainElement in terrainElementList:
                    terrainElement.move(xDirection, yDirection)
            else:
                terrainElementList.move(xDirection, yDirection)

    def update(self, player):
        # detecte les collisions avec le joueur
        for terrainElementList in self.terrainElements:  # iterate through all the terrainelements
            if hasattr(terrainElementList, '__iter__'):  # if its iterable
                for terrainElement in terrainElementList:
                    terrainElement.update(player)
            else:
                terrainElementList.update(player)

    def draw(self, screen):
        for terrainElementList in self.terrainElements:  # iterate through all the terrainelements
            if hasattr(terrainElementList, '__iter__'):  # if its iterable
                for terrainElement in terrainElementList:
                    terrainElement.draw(screen)
            else:
                terrainElementList.draw(screen)

    def setSprites(self, dayOrNight):
        for terrainElementList in self.terrainElements:  # iterate through all the terrainelements
            if hasattr(terrainElementList, '__iter__'):  # if its iterable
                for terrainElement in terrainElementList:
                    terrainElement.toggleSprite(dayOrNight)
            else:
                terrainElementList.toggleSprite(dayOrNight)
