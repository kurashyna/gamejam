import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
running = True
# j'ai enlevé le .convert() pour avoir la transparence
image = pygame.image.load("test.png")
clock = pygame.time.Clock()

x = 0
y = 0

while running:
    for event in pygame.event.get():  # recupere tous les evenements
        # evenement retourné lorsque l'on clique sur la croix dans windows, fait sortir de la boucle et ainsi ferme le jeu
        if event.type == pygame.QUIT:
            running = False
        # ancienne methode pour gerer les evenements, j'ai changé en utilisant get_pressed() pour que ca s'active tant que les touches sont enfoncées
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
        x -= 5
    if pressed[pygame.K_RIGHT]:
        x += 5
    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5

    screen.fill((27, 27, 27))
    screen.blit(image, (x, y))  # affichage de l'image aux coordonées x,y
    pygame.display.flip()  # actualise tout la fenetre
    clock.tick(60)  # permet de set le framerate

pygame.quit()
