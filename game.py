import pygame
# from gameover import GameOver
from hud import HUD
# from introduction import Intro
from player import Player
from terrain import Terrain
from environment import Environment
# import menu
# import shelve



class Game:

    def __init__(self, screen, menu):  # constructeur
        self.menu = menu
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
        self.screen.fill((173, 188, 58))
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
        # file = shelve.open('highscore/highscore.dat')
        # if self.hud.score.value > file['score']:
        #     file['score'] = self.hud.score.value
        # print(file['score'])
        # file.close()

        # print("t nul")
        
        self.menu.game_over()

        pygame.quit() #quit the intro when starting the game


    def getTerrain(self):
        return self.terrain
