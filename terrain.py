import pygame
from obstacle import Obstacle


class Terrain:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/sprites/png/background/terrain.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.obstacle = Obstacle(500, 300)

    def update(self, player):
        # detecte les collisions avec le joueur
        self.obstacle.update(player)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.obstacle.draw(screen)
