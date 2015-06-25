import pygame
import resources as R

class Object(pygame.sprite.Sprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		types = {
			'cup': [R.IMAGES['cup.png'], False],
			'glass': [R.IMAGES['glass.png'], True]
		}

		self.image = types[typ][0]
		self.rect = self.image.get_rect()
		
		#position
		self.rect.x = x
		self.rect.y = y + 64 - self.image.get_height()

		self.type = "object"
		self.deadly = types[typ][1]
		self.species = typ
		self.picked_up = False

	def update(self, dt, bg_pos):
		""" update the position of the enemy
			so that it moves back and forth
		"""
		pass

