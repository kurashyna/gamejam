import pygame
from obstacle import Obstacle


class Terrain:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/sprites/png/background/terrain.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.obstacles = [Obstacle(500, 300), Obstacle(200, 300)]

    def update(self, player):
        # detecte les collisions avec le joueur
        for obstacle in self.obstacles:
            obstacle.update(player)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
