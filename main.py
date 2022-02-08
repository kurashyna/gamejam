import pygame
from fruit import Fruit
from hud import HUD
from player import Player
from terrain import Terrain
from obstacle import Obstacle


class Game:
    def __init__(self, screen):  # constructeur
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(self, 500, 360)
        self.hud = HUD(screen, self.player)
        self.terrain = Terrain(self, self.player)

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


pygame.init()
screen = pygame.display.set_mode((1080, 720))
game = Game(screen)  # instantiation de l'objet
game.run()  # lancement du jeu
pygame.quit()
