import pygame
import sys
import game
from button import Button


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.game = game.Game(screen)
        self.score = self.game.hud.score.value



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
            self.game.run()  # lancement du jeu
            pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def display_score(self,score_val):
        #coordonnées
        score_x, score_y = 200, 550
        #conversion en str
        score_val= str(score_val)
        font = pygame.font.Font('freesansbold.ttf', 30)
        score = font.render(("Score :" + score_val), True, (255, 255, 255))
        self.screen.blit(score,(score_x, score_y))


    def game_over(self):
        running = True
        while (running):
            # chagement logo & titre fenetre
            pygame.display.set_caption('Loser')
            logo_icon = pygame.image.load("assets/sprites/png/title.png")
            pygame.display.set_icon(logo_icon)

            # couleur de fond
            self.screen.fill((0, 0, 0))

            # logo
            Text = pygame.image.load("assets/sprites/png/game_over_title.png")
            self.screen.blit(Text, (200, 100))

            #recupere le score
            self.score = self.game.hud.score.value
            self.display_score(self.score)

            # boutons
            play_again_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/play_again_button.png"), x=520, y=400)
            menu_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/menu_button.png"), x=520, y=500)
            quit_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/quit_button.png"), x=520, y=600)
            # position de la souris
            mouse_position = pygame.mouse.get_pos()

            play_again_button.update(self.screen)
            menu_button.update(self.screen)
            quit_button.update(self.screen)


            # on verifie quel bouton à été cliqué
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if play_again_button.buttonClicked(mouse_position):
                        self.play()
                    # Pour menu button
                    if menu_button.buttonClicked(mouse_position):
                        self.main_menu()
                    # pour quit button
                    if quit_button.buttonClicked(mouse_position):
                        running = False

            pygame.display.update()
        pygame.quit()