import pygame
from game import Game
from button import Button

pygame.init()
screen = pygame.display.set_mode((1080, 720))
# tite de la fênetre
pygame.display.set_caption("Main Menu")
# chaque fonction va afficher une fenetre diff et chac  une a une boucle de jeu differentes
# pour passer d'une à l'autre il suffit de changer le background en noir


def main_menu():
    running = True
    while(running):
        screen.fill((116, 190, 88))

        # cadre fond
        cadre = pygame.image.load('assets/sprites/png/menu_cadre.png')
        screen.blit(cadre, (140, 60))

        # logo
        logo = pygame.image.load('assets/sprites/png/title-large.png')
        screen.blit(logo, (280, 50))

        # boutons
        start_button = Button(image=pygame.image.load(
            "assets/sprites/png/buttons/Start_Game_button.png"), x=520, y=300)
        options_button = Button(image=pygame.image.load(
            "assets/sprites/png/buttons/options_button.png"), x=520, y=400)
        quit_button = Button(image=pygame.image.load(
            "assets/sprites/png/buttons/quit_button.png"), x=520, y=500)
        # position de la souris
        mouse_position = pygame.mouse.get_pos()

        start_button.update(screen)
        options_button.update(screen)
        quit_button.update(screen)

        # on verifie quel bouton à été cliqué
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Pour Start game button
                if start_button.buttonClicked(mouse_position):
                    play()
                # Pour option button
                elif options_button.buttonClicked(mouse_position):
                    options()
                # pour quit button
                elif quit_button.buttonClicked(mouse_position):
                    running = False

        pygame.display.update()

    pygame.quit()


def options():
    running = True
    while running:
        pygame.display.set_caption("Options")
        screen.fill((116, 190, 88))

        # cadre fond
        cadre = pygame.image.load('assets/sprites/png/menu_cadre.png')
        screen.blit(cadre, (140, 60))

        # logo
        logo = pygame.image.load('assets/sprites/png/title-large.png')
        screen.blit(logo, (280, 50))

        # boutons
        back_button = Button(image=pygame.image.load(
            "assets/sprites/png/buttons/back_button.png"), x=500, y=450)
        back_button.update(screen)

        # position de la souris
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.buttonClicked(mouse_position):
                    main_menu()

        pygame.display.update()


def play():
    pygame.display.set_caption("Devil Fruit")
    running = True
    while(running):
        screen = pygame.display.set_mode((1080, 720))
        game = Game(screen)  # instantiation de l'objet
        game.run()  # lancement du jeu
        pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main_menu()
