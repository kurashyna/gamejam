import pygame
from terrainelement import *
import random


class Terrain:
    def __init__(self, game, player):
        self.player = player
        self.ground = Ground(0, 0)
        self.effects = []
        self.projectiles = []
        self.obstacles = []
        treeNumberX = 0
        # generating trees at the border of the map
        while True:
            newTree = Obstacle(self, treeNumberX * 5 * 32, 0, 5, "tree")
            if newTree.rect.colliderect(self.ground):
                self.obstacles.append(newTree)
                treeNumberX += 1
            else:
                break
        treeNumberY = 1
        while True:
            newTree = Obstacle(self, 0, treeNumberY * 5 * 29, 5, "tree")
            if newTree.rect.colliderect(self.ground):
                self.obstacles.append(newTree)
                treeNumberY += 1
            else:
                break
        treeNumberY -= 1
        treeNumberX = 1
        while True:
            newTree = Obstacle(self, treeNumberX * 5 * 32, treeNumberY * 5 * 29, 5, "tree")
            if newTree.rect.colliderect(self.ground):
                self.obstacles.append(newTree)
                treeNumberX += 1
            else:
                break

        treeNumberX -= 1
        treeNumberY = 1
        while True:
            newTree = Obstacle(self, treeNumberX * 5 * 32, treeNumberY * 5 * 29, 5, "tree")
            if newTree.rect.colliderect(self.ground):
                self.obstacles.append(newTree)
                treeNumberY += 1
            else:
                break



        for i in range(7):
            while True:
                newObstacle = Obstacle(self, random.randrange(0, 4400), random.randrange(0, 2800), 5, "mill")
                isColliding = False
                for obstacle in self.obstacles:
                    if newObstacle.rect.colliderect(obstacle.rect):
                        isColliding = True
                # so that the player doesnt spawn in an obstacle
                if not newObstacle.rect.colliderect(player.rect) and not isColliding:
                    break
            self.obstacles.append(newObstacle)
        self.fruits = []
        self.terrainElements = [self.ground,
                                self.obstacles, self.effects, self.fruits, self.projectiles]

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
