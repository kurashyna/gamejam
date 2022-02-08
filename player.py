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
        self.isBouncing = False
        self.bounceMoment = 0
        self.maxHP = 8
        self.currentHP = self.maxHP  # start with healthbar full

    def handle_events(self, event):
        if not self.isBouncing:  # to prevent going out of bound
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
        if self.isBouncing:
            if pygame.time.get_ticks() > self.bounceMoment + 100:
                self.isBouncing = False

        self.move()

    def move(self):
        self.game.terrain.move(-(self.velocity[0] *
                               self.speed), -(self.velocity[1] * self.speed))

    def bounce(self):
        self.isBouncing = True
        self.bounceMoment = pygame.time.get_ticks()
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def addDash(self):
        self.dashsAvailable += 1
        print(self.dashsAvailable)
        self.game.hud.powerUpBar.addDash()  # add the dash icon to the hud

    def dash(self):
        self.speed = 15
        # get the moment when the dash was used
        self.dashUseMoment = pygame.time.get_ticks()
        self.isDashing = True
        self.dashsAvailable -= 1
        self.game.hud.powerUpBar.removeDash()  # add the dash icon to the hud

    def draw(self, screen):
        screen.blit(self.image, self.rect)
