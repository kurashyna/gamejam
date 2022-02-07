import pygame

class Player:
    playerImg = pygame.image.load("../sprites/png/pear.png")
    x = 0
    y = 0
    speed = 1

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.speed = 1

    def move(self, direction):
        if direction == "gauche":
            self.x -= self.speed
        if direction == "droite":
            self.x += self.speed
        if direction == "haut":
            self.y += self.speed
        if direction == "bas":
            self.y -= self.speed
