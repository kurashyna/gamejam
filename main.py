import pygame
from player import Player


class Game:
    def __init__(self, screen):  # constructeur
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0)

    def handling_events(self):
        for event in pygame.event.get():  # recupere tous les evenements
            # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            if event.type == pygame.QUIT:
                self.running = False

        # movement inputs
        pressed = pygame.key.get_pressed()
        # axe x
        if pressed[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif pressed[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0
        # axe y
        if pressed[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif pressed[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

    def update(self):
        self.player.move()

    def display(self):
        self.screen.fill((27, 27, 27))
        self.player.draw(self.screen)
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
