import imp


import pygame


class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y),
                         (self.x + 100, self.y))
