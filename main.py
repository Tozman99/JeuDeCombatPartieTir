import pygame
import sys, time
from pygame.sprite import Group
from joueur import Joueur
from sol import Sol
from projectiles import Projectile

class Jeu:

	def __init__(self):

		self.ecran = pygame.display.set_mode((1100, 600))
		pygame.display.set_caption('Jeu De Combat')
		self.jeu_encours = True
		self.joueur_x, self.joueur_y = 600, 100
		self.taille = [32, 64]
		self.joueur_vitesse_x = 0
		self.joueur = Joueur(self.joueur_x, self.joueur_y, self.taille)
		self.sol = Sol()
		self.gravite = (0, 10)
		self.resistance = (0, 0)
		self.rect = pygame.Rect(0, 0, 1100, 600)
		self.collision_sol = False
		self.horloge = pygame.time.Clock()
		self.fps = 30
		self.projectiles_groupe = Group()
		self.t1, self.t2 = 0, 0
		self.delta_temps = 0

	def boucle_principale(self):
		"""
		Boucle principale du jeu

		"""

		while self.jeu_encours:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.joueur_vitesse_x = 10
						self.joueur.direction = 1

					if event.key == pygame.K_LEFT:
						self.joueur_vitesse_x = -10
						self.joueur.direction = -1


					if event.key == pygame.K_UP:
						self.joueur.a_sauter = True
						self.joueur.nombre_de_saut += 1

					if event.key == pygame.K_p:
						self.t1 = time.time()


				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						self.joueur_vitesse_x = 0

					if event.key == pygame.K_LEFT:

						self.joueur_vitesse_x = 0

					if event.key == pygame.K_p:
						self.t2 = time.time()
						self.joueur.a_tire = True

			if self.sol.rect.colliderect(self.joueur.rect):
				self.resistance = (0, -10)
				self.collision_sol = True
				self.joueur.nombre_de_saut = 0

			else:
				self.resistance = (0, 0)

			if self.joueur.a_sauter and self.collision_sol:
				if self.joueur.nombre_de_saut < 2:
					self.joueur.sauter()
			self.delta_temps = self.t2 - self.t1
			self.joueur.mouvement(self.joueur_vitesse_x)
			self.gravite_jeu()
			#self.joueur.sauter()
			self.joueur.rect.clamp_ip(self.rect)
			self.ecran.fill((255, 255, 255))
			self.joueur.afficher(self.ecran)
			self.sol.afficher(self.ecran)
			pygame.draw.rect(self.ecran, (255, 0, 0), self.rect, 1)
			self.horloge.tick(self.fps)
			pygame.display.flip()

	def gravite_jeu(self):
		"""
		Gére la gravité pour chaque élément
		"""

		self.joueur.rect.y += self.gravite[1] + self.resistance[1]


if __name__ == '__main__':
	pygame.init()
	Jeu().boucle_principale()
	pygame.quit()
