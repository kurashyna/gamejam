import pygame
from fruit import Fruit
from player import Player
from terrain import Terrain
from obstacle import Obstacle


class Game:
    def __init__(self, screen):  # constructeur
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(self, 0, 0)
        self.terrain = Terrain(0, 0)
        self.fruits = [Fruit(self, 700, 200), Fruit(self, 300, 200)]

        # booleans used to prevent diagonal movement
        self.xIsPressed = False
        self.yIsPressed = False

    def handling_events(self):
        for event in pygame.event.get():  # recupere tous les evenements
            # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_events(event)

        # # movement inputs
        # pressed = pygame.key.get_pressed()
        # # axe x

        # if pressed[pygame.K_LEFT]:
        #     self.player.velocity[0] = -1
        #     xIsPressed = True
        # elif pressed[pygame.K_RIGHT]:
        #     self.player.velocity[0] = 1
        #     xIsPressed = True
        # else:
        #     self.player.velocity[0] = 0
        #     xIsPressed = False

        # if pressed[pygame.K_UP]:
        #     self.player.velocity[1] = -1
        #     yIsPressed = True
        # elif pressed[pygame.K_DOWN]:
        #     self.player.velocity[1] = 1
        #     yIsPressed = True
        # else:
        #     self.player.velocity[1] = 0
        #     yIsPressed = False

    def update(self):
        self.player.update()
        self.terrain.update(self.player)
        for fruit in self.fruits:
            fruit.update(self.player)

    def display(self):
        self.screen.fill((27, 27, 27))
        self.terrain.draw(self.screen)
        self.player.draw(self.screen)
        for fruit in self.fruits:
            fruit.draw(self.screen)
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
