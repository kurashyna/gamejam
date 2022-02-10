import pygame


class Healthbar:
    hearths = []
    def __init__(self):
        # healthbar is made of 4 hearths icons

        self.offset = 60  # space between each hearth
        for i in range(4):
            self.hearths.append(Hearth(100 + (i*self.offset), 600))

    def draw(self, screen):
        for hearth in self.hearths:
            hearth.draw(screen)

    def loseHP(self, amount):
        for i in range(amount):
            self.hearths.pop()

    def gainHP(self, amount):
        self.hearths.append(Hearth(100 + (len(self.hearths)*self.offset), 600))
        print(len(self.hearths))


class Hearth:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/sprites/png/hud/heart/filled-heart.png")
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
