import pygame


class Projectile(pygame.sprite.Sprite):

	def __init__(self, x, y, taille, direction, image):

		self.x = x
		self.y = y
		self.taille = taille
		self.direction = direction
		self.image = image
		self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])

	def afficher(self, surface):

		pygame.draw.rect(surface, (255, 0, 255), self.rect)

	def mouvement(self, vitesse):

		# -1 alors vitesse est negative => deplacement du projectile vers la gauche
		# 1 alors vitesse positive => deplacement du projectile vers la droite

		self.rect.x += (vitesse * self.direction)
