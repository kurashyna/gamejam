import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
running = True
image = pygame.image.load("fond.jpg")
imagenuit = pygame.image.load("nuit.jpg")
clock = pygame.time.Clock()

x = 0
y = 0

while running:
    for event in pygame.event.get():  # recupere tous les evenements
        if event.type == pygame.QUIT:  # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         print("gauche")
        #     if event.key == pygame.K_RIGHT:
        #         print("droite")
        #     if event.key == pygame.K_UP:
        #         print("haut")
        #     if event.key == pygame.K_DOWN:
        #         print("bas")
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_SPACE]:
        y -= 150
        screen.blit(imagenuit, (x, y))
        pygame.display.flip()
        pygame.time.wait(1000)
        y += 150
        screen.blit(imagenuit, (x, y))
        pygame.display.flip()
    screen.fill((27, 27, 27))
     # affichage de l'image aux coordonées x,y
    screen.blit(image, (0, 0))
    screen.blit(imagenuit, (x, y))
    pygame.display.flip()  # actualise tout la fenetre
    clock.tick(60)  # permet de set le framerate

pygame.quit()
