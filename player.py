import pygame
from terrain import *

class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.hud = game.hud
        assetFolder = "assets/sprites/png/characters/"
        self.scale = 1
        self.image = pygame.image.load(assetFolder + "knight_standing_0.png")
        self.size = self.image.get_size()  # obtient la taille de l'image
        self.animations = {
            "forward": [],
            "backward": [],
            "left": [],
            "right": [],
            "standing": [],
        }
        for key in self.animations:
            for i in range(4):
                self.animations[key].append(pygame.image.load(
                    assetFolder + "knight_" + key + "_" + str(i) + ".png"))

        self.currentAnimationFrame = 0
        self.delayBetweenFrames = 100
        self.lastTimeFrameChanged = 0
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 10
        self.currentSpeed = self.speed
        self.velocity = [0, 0]
        # dash
        self.dashsAvailable = 0
        self.dashUseMoment = 0
        self.isDashing = False
        self.isBouncing = False
        self.bounceMoment = 0
        self.maxHP = 4
        self.currentHP = self.maxHP  # start with healthbar full
        #freezeAllAvailable
        self.freezeAllAvailable =0
    # virtual methods
    def setScale(self):
        self.image = pygame.transform.scale(self.image, (int(
            self.size[0]*self.scale), int(self.size[1]*self.scale)))  # multiplie la taille de x et y par 5

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
                if event.key == pygame.K_f and self.freezeAllAvailable > 0:
                    self.freezeAll()

    def update(self):
        currentTime = pygame.time.get_ticks()
        if self.isDashing:
            if pygame.time.get_ticks() > self.dashUseMoment + 300:
                self.currentSpeed = self.speed
                self.isDashing = False
        if self.isBouncing:
            if pygame.time.get_ticks() > self.bounceMoment + 20:
                self.isBouncing = False
        # animation

        if currentTime > self.lastTimeFrameChanged + self.delayBetweenFrames:
            # direction
            if self.velocity[1] > 0:
                direction = "forward"
            elif self.velocity[1] < 0:
                direction = "backward"
            elif self.velocity[0] > 0:
                direction = "right"
            elif self.velocity[0] < 0:
                direction = "left"
            else:
                direction = "standing"
            if self.currentAnimationFrame == len(self.animations["forward"]) - 1:
                self.currentAnimationFrame = 0
            else:
                self.currentAnimationFrame += 1
            # change frame
            self.image = self.animations[direction][self.currentAnimationFrame]
            self.setScale()
            self.lastTimeFrameChanged = currentTime

        # movement
        self.move()

    def move(self):
        self.game.terrain.move(-(self.velocity[0] *
                               self.currentSpeed), -(self.velocity[1] * self.currentSpeed))

    def bounce(self):
        self.isBouncing = True
        self.bounceMoment = pygame.time.get_ticks()
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def addDash(self):
        self.dashsAvailable += 1
        self.game.hud.powerUpBar.addDash(self)  # add the dash icon to the hud

    def addFreezeall(self):
        self.freezeAllAvailable += 1
        self.game.hud.powerUpBar.addFreeze(self)

    def addScore(self, scoreAmount):
        self.game.hud.score.addValue(scoreAmount)

    def mouvementspeedbuff(self):
        self.speed = self.speed+2

    def dash(self):
        self.currentSpeed = self.speed*2
        # get the moment when the dash was used
        self.dashUseMoment = pygame.time.get_ticks()
        self.isDashing = True
        self.dashsAvailable -= 1
        self.game.hud.powerUpBar.removeDash()  # add the dash icon to the hud

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def loseHP(self):
        self.currentHP = self.currentHP - 1
        self.hud.loseHP(1)
        if self.currentHP <= 0:
            self.game.gameOver()

    def recoveryhp(self):
        self.currentHP = self.currentHP + 1
        self.hud.gainHP(1)

    def freezeAll(self) :
        print("freeze")
        for projectile in self.game.terrain.terrainElements[4] :
            projectile.freeze = True
        self.freezeAllAvailable =self.freezeAllAvailable-1
        self.game.hud.powerUpBar.removeFreeze()
