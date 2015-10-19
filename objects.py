import pygame
import resources as R

class Object(pygame.sprite.Sprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		object_dict = {
			'cup': [R.IMAGES['cup.png'], False, 1],
			'glass': [R.IMAGES['glass.png'], True, 0]
		}

		self.image = object_dict[typ][0]
		self.rect = self.image.get_rect()
		
		# position
		self.rect.left = x
		self.rect.top = y + 64 - self.image.get_height()

		# attributes of the object
		self.deadly = object_dict[typ][1]
		self.health = object_dict[typ][2]
		self.species = typ
		self.picked_up = False

	def update(self, dt, bg_pos):
		""" update the position of the object
		"""
		pass

