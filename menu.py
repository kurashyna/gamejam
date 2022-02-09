import pygame
from game import Game
from button import Button

class Menu:

    def __init__(self, screen):
        self.screen = screen

    def main_menu(self):
        running = True
        while(running):

            pygame.display.set_caption('Menu')
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)

            self.screen.fill((116, 190, 88))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/menu_cadre.png')
            self.screen.blit(cadre, (140, 60))

            # logo
            logo = pygame.image.load('assets/sprites/png/title-large.png')
            self.screen.blit(logo, (280, 50))

            # boutons
            start_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/Start_Game_button.png"), x=520, y=300)
            options_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/options_button.png"), x=520, y=400)
            quit_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/quit_button.png"), x=520, y=500)
            # position de la souris
            mouse_position = pygame.mouse.get_pos()

            start_button.update(self.screen)
            options_button.update(self.screen)
            quit_button.update(self.screen)

            # on verifie quel bouton à été cliqué
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if start_button.buttonClicked(mouse_position):
                        self.play()
                    # Pour option button
                    elif options_button.buttonClicked(mouse_position):
                        self.options()
                    # pour quit button
                    elif quit_button.buttonClicked(mouse_position):
                        running = False

            pygame.display.update()
        pygame.quit()


    def options(self):
        running = True
        while running:
            pygame.display.set_caption("Options")
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)
            self.screen.fill((116, 190, 88))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/menu_cadre.png')
            self.screen.blit(cadre, (140, 60))

            # logo
            logo = pygame.image.load('assets/sprites/png/title-large.png')
            self.screen.blit(logo, (280, 50))

            # boutons
            back_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/back_button.png"), x=500, y=450)
            back_button.update(self.screen)

            # position de la souris
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.buttonClicked(mouse_position):
                        self.main_menu()

            pygame.display.update()


    def play(self):
        pygame.display.set_caption("Devil Fruit")
        logo_icon = pygame.image.load('assets/sprites/png/title.png')
        pygame.display.set_icon(logo_icon)
        running = True
        while(running):
            screen = pygame.display.set_mode((1080, 720))
            game = Game(screen)  # instantiation de l'objet
            game.run()  # lancement du jeu
            pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



pygame.init()
screen = pygame.display.set_mode((1080, 720))
menu = Menu(screen)  # instantiation de l'objet
menu.main_menu()
pygame.quit()