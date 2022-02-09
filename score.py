import pygame


class Score:
    def __init__(self):
        self.value = 0
        self.white = (255, 255, 255)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.value), True, self.white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (pygame.display.get_surface().get_rect(
        ).right - 200, pygame.display.get_surface().get_rect().top + 50)

    def update(self):
        self.value = pygame.time.get_ticks()
        self.text = self.font.render(str(self.value), True, self.white)

    def draw(self, screen):
        screen.blit(self.text, self.textRect)
