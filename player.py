import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/sprites/png/characters/knight.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]

    def move(self):
        self.rect.move_ip(
            self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
