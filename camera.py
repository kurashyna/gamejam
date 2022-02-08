import pygame
vec = pygame.math.Vector2


class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = vec(0, 0)
