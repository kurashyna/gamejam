import pygame


class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.image.load(
            "assets/sprites/png/characters/knight.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]
        # dash
        self.dashsAvailable = 0
        self.dashUseMoment = 0
        self.isDashing = False
        self.maxHP = 8
        self.currentHP = self.maxHP  # start with healthbar full

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            # movement
            if event.key == pygame.K_LEFT:
                self.velocity = [-1, 0]
            if event.key == pygame.K_RIGHT:
                self.velocity = [1, 0]
            if event.key == pygame.K_UP:
                self.velocity = [0, -1]
            if event.key == pygame.K_DOWN:
                self.velocity = [0, 1]
            # dash
            if event.key == pygame.K_SPACE and self.dashsAvailable > 0:
                self.dash()

    def update(self):
        if self.isDashing:
            if pygame.time.get_ticks() > self.dashUseMoment + 300:
                self.speed = 5
                self.isDashing = False
        self.move()

    def move(self):
        self.rect.move_ip(
            self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def addDash(self):
        self.dashsAvailable += 1
        print(self.dashsAvailable)

    def dash(self):
        self.speed = 15
        self.dashUseMoment = pygame.time.get_ticks()
        self.isDashing = True
        self.dashsAvailable -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
