import pygame


class Fruit:
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.image.load(
            "assets/sprites/png/fruits/pear.png")
        self.size = self.image.get_size()  # obtient la taille de l'image
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0]*5), int(self.size[1]*5)))  # multiplie la taille de x et y par 5
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.addDash()
            self.getEaten()

    def getEaten(self):
        self.game.fruits.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
