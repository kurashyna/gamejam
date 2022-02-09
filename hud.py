import pygame

from healthbar import Healthbar
from powerupbar import PowerUpBar
from score import Score


class HUD:
    # contient tous les elements de l'hud: hp, mana...
    def __init__(self, screen, game):
        self.player = game.player
        self.healthbar = Healthbar()
        self.powerUpBar = PowerUpBar(game.player)
        self.rect = screen.get_rect()
        self.score = Score()

    def draw(self, screen):
        self.healthbar.draw(screen)
        self.powerUpBar.draw(screen)
        self.score.draw(screen)

    def update(self):
        self.score.update()
