import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
running = True
image = pygame.image.load("test.png").convert()

while running:
    for event in pygame.event.get():  # recupere tous les evenements
        if event.type == pygame.QUIT:  # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            running = False
    screen.blit(image, (0, 0))  # affichage de l'image aux coordonées 0,0
    pygame.display.flip()  # actualise tout la fenetre

pygame.quit()
