import pygame
""" import classPlayer """

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
image = pygame.image.load("../fond.jpg")
clock = pygame.time.Clock()

class Player:
    playerImg = pygame.image.load("../sprites/png/pear.png")
    x = 0
    y = 0
    speed = 1

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.speed = 1

    def move(self,):
        if pressed[pygame.K_LEFT]:
            self.x -= self.speed
        if pressed[pygame.K_RIGHT]:
            self.x += self.speed
        if pressed[pygame.K_UP]:
            self.y += self.speed
        if pressed[pygame.K_DOWN]:
            self.y -= self.speed

while running:
    for event in pygame.event.get():  # recupere tous les evenements
        if event.type == pygame.QUIT:  # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            running = False
    pressed = pygame.key.get_pressed()
    player = Player()

    if pressed[pygame.K_LEFT]:
        player.move()
    if pressed[pygame.K_RIGHT]:
        player.move()
    if pressed[pygame.K_UP]:
        player.move()
    if pressed[pygame.K_DOWN]:
        player.move()

    screen.fill((27, 27, 27))
     # affichage de l'image aux coordonées x,y
    screen.blit(player.playerImg, (0, 0))
    pygame.display.flip()  # actualise tout la fenetre
    clock.tick(60)  # permet de set le framerate

pygame.quit()
