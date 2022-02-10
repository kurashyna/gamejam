import pygame
from button import Button


class GameOver:

    def __init__(self, screen):
        self.screen = screen

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

            # boutons
            play_again_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/play_again_button.png"), x=520, y=300)
            menu_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/menu_button.png"), x=520, y=400)
            quit_button = Button(image=pygame.image.load(
                "assets/sprites/png/buttons/quit_button.png"), x=520, y=500)
            # position de la souris
            mouse_position = pygame.mouse.get_pos()

            play_again_button.update(self.screen)
            menu_button.update(self.screen)
            quit_button.update(self.screen)

            # instancie menu
            menu = Menu(self.screen)
            # on verifie quel bouton à été cliqué
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pour Start game button
                    if menu_button.buttonClicked(mouse_position):
                        menu.play()
                    # Pour menu button
                    if menu_button.buttonClicked(mouse_position):
                        menu.main_menu()
                    # pour quit button
                    if quit_button.buttonClicked(mouse_position):
                        running = False

            pygame.display.update()
        pygame.quit()


# pygame.init()
# screen = pygame.display.set_mode((1080, 720))
# end = GameOver(screen)  # instantiation de l'objet
# end.game_over()
# pygame.quit()
