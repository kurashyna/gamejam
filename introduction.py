import pygame
from button import Button
import menu

class Intro:
    def __init__(self, screen):
        self.screen = screen

    def view_1(self):
        running = True
        while (running):
            pygame.display.set_caption('Devil Fruits')
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)

            self.screen.fill((0, 0, 0))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/intro/Intro-1.png')
            self.screen.blit(cadre, (140, 10))

            logo = pygame.image.load('assets/sprites/png/intro/title_huge.png')
            self.screen.blit(logo, (225, 80))

            # boutons
            start_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/start_button.png"), x=550, y=450)
            play_now_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/play_now_button.png"), x=550, y=550)

            mouse_position = pygame.mouse.get_pos()

            start_button.update(self.screen)
            play_now_button.update(self.screen)

            # instancie menu
            m = menu.Menu(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if start_button.buttonClicked(mouse_position):
                        self.view_2()
                    if play_now_button.buttonClicked(mouse_position):
                        m.play()

            pygame.display.update()

        pygame.quit()

    def view_2(self):
        running = True
        while (running):
            pygame.display.set_caption('Devil Fruits')
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)

            self.screen.fill((0, 0, 0))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/intro/Intro-2.png')
            self.screen.blit(cadre, (140, 10))

            continue_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/continue_button.png"), x=700, y=600)
            skip_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/skip_button_view2.png"), x=420, y=600)

            mouse_position = pygame.mouse.get_pos()

            continue_button.update(self.screen)
            skip_button.update(self.screen)

            # instancie menu
            m = menu.Menu(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if continue_button.buttonClicked(mouse_position):
                        self.view_3()
                    if skip_button.buttonClicked(mouse_position):
                        m.main_menu()

            pygame.display.update()

        pygame.quit()

    def view_3(self):
        running = True
        while (running):
            pygame.display.set_caption('Devil Fruits')
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)

            self.screen.fill((0, 0, 0))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/intro/Intro-3.png')
            self.screen.blit(cadre, (140, 10))

            skip_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/skip_button_view3.png"), x=420, y=600)
            continue_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/continue_button_view3.png"), x=700, y=600)

            mouse_position = pygame.mouse.get_pos()

            continue_button.update(self.screen)
            skip_button.update(self.screen)

            # instancie menu
            m = menu.Menu(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if continue_button.buttonClicked(mouse_position):
                        self.view_4()
                    if skip_button.buttonClicked(mouse_position):
                        m.main_menu()

            pygame.display.update()

        pygame.quit()

    def view_4(self):
        running = True
        while (running):
            pygame.display.set_caption('Devil Fruits')
            logo_icon = pygame.image.load('assets/sprites/png/title.png')
            pygame.display.set_icon(logo_icon)

            self.screen.fill((0, 0, 0))

            # cadre fond
            cadre = pygame.image.load('assets/sprites/png/intro/Intro-4.png')
            self.screen.blit(cadre, (140, 10))

            main_menu_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/main_menu_button.png"), x=420, y=600)
            start_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/Start_Game_button.png"), x=700, y=600)

            mouse_position = pygame.mouse.get_pos()

            main_menu_button.update(self.screen)
            start_button.update(self.screen)

            # instancie menu
            m = menu.Menu(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if start_button.buttonClicked(mouse_position):
                        m.play()
                    if start_button.buttonClicked(mouse_position):
                        m.main_menu()

            pygame.display.update()

        pygame.quit()


pygame.init()
screen = pygame.display.set_mode((1080, 720))
intro = Intro(screen)  # instantiation de l'objet
intro.view_1()
pygame.quit()
