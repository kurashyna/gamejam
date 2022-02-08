import pygame

from healthbar import Healthbar
from powerupbar import PowerUpBar


class HUD:
    # contient tous les elements de l'hud: hp, mana...
    def __init__(self, screen, player):
        self.player = player
        self.healthbar = Healthbar()
        self.powerUpBar = PowerUpBar(player)
        self.rect = screen.get_rect()

    def draw(self, screen):
        self.healthbar.draw(screen)
        self.powerUpBar.draw(screen)
