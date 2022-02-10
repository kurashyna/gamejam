import pygame


class PowerUpBar:
    def __init__(self):
        # healthbar is made of 4 hearths icons
        self.dashCharges = []
        self.offset = 60  # space between each hearth

    def addDash(self, player):
        self.dashCharges.append(DashCharge(
            700 + (player.dashsAvailable*self.offset), 600))

    def removeDash(self):
        self.dashCharges.pop()

    def draw(self, screen):
        for dashCharge in self.dashCharges:
            dashCharge.draw(screen)


class DashCharge:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/sprites/png/hud/pear.png")
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
