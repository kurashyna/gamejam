import pygame
class Button():
	#buttons a utiliser pour les vues
	def __init__(self,image, x, y):
		self.image = image
		self.x = x
		self.y = y
		#rectangle representant la surface du bouton
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def update(self, screen):
		screen.blit(self.image, self.rect)

	def buttonClicked(self, mousePos):
		#coordonnées de la souris
		mX = mousePos[0]
		mY= mousePos[1]
		#si coordonnées souris sur la surface de l'image
		if mX in range(self.rect.left, self.rect.right) and mY in range(self.rect.top, self.rect.bottom):
			print("clic")
			return True
		else:
			return False

