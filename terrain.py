import pygame
from terrainelement import *


class Terrain:
    def __init__(self, game, player):
        self.player = player

        self.ground = Ground(0, 0)
        self.obstacles = [Obstacle(800, 300, 5), Obstacle(200, 300, 3)]
        self.fruits = [Fruit(self, 700, 200, 1), Fruit(self, 300, 200, 2)]
        self.terrainElements = [self.ground, self.obstacles, self.fruits]

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
                    # ground has no update method so no else
                    terrainElement.update(player)
            else :
                terrainElementList.update(player)
    def draw(self, screen):
        for terrainElementList in self.terrainElements:  # iterate through all the terrainelements
            if hasattr(terrainElementList, '__iter__'):  # if its iterable
                for terrainElement in terrainElementList:
                    terrainElement.draw(screen)
            else:
                terrainElementList.draw(screen)
