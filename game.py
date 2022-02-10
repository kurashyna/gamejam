import pygame
from hud import HUD
from player import Player
from terrain import Terrain
from environment import Environment
from gameover import GameOver
import shelve



class Game:

    def __init__(self, screen):  # constructeur
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.hud = HUD(screen, self)
        self.player = Player(self, 500, 360)
        self.terrain = Terrain(self, self.player)
        self.environment = Environment(self)
        # booleans used to prevent diagonal movement
        self.xIsPressed = False
        self.yIsPressed = False

    def handling_events(self):
        for event in pygame.event.get():  # recupere tous les evenements
            # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_events(event)

    def update(self):
        self.player.update()
        self.terrain.update(self.player)
        self.environment.update()
        self.hud.update()

    def display(self):
        self.screen.fill((71, 71, 71))
        self.terrain.draw(self.screen)
        self.player.draw(self.screen)
        self.hud.draw(self.screen)
        pygame.display.flip()

    def run(self):  # methode run
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

    def gameOver(self):
        file = shelve.open('highscore/highscore')
        if self.hud.score.value > file['score']:
            file['score'] = self.hud.score.value
        print(file['score'])
        file.close()

        print("t nul")
        # end = GameOver(self.screen)
        # end.game_over()
    def getTerrain(self):
        return self.terrain
