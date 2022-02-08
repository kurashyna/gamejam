import pygame

from healthbar import Healthbar


class HUD:
    # contient tous les elements de l'hud: hp, mana...
    def __init__(self, screen):
        self.healthbar = Healthbar(200, 600)
        self.rect = screen.get_rect()

    def draw(self, screen):
        self.healthbar.draw(screen)
