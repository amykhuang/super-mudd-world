import pygame
import resources as R

class Tile(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = R.IMAGES['tile.png']
		self.rect = self.image.get_rect()
		self.vel = [0,0]
		self.deadly = False

class Ground(Tile):
	def __init__(self, x, y):
		Tile.__init__(self, x, y)
		self.image = R.IMAGES['tile.png']
		self.species = "platform"
		self.rect.left = x
		self.rect.top = y

class Platform(Tile):
	def __init__(self, x, y):
		Tile.__init__(self, x, y)
		self.image = R.IMAGES['platform.png']
		self.species = "platform"
		self.rect.left = x
		self.rect.top = y

class Spike(Tile):
	def __init__(self, x, y):
		Tile.__init__(self, x, y)
		self.image = R.IMAGES['platform.png']
		self.species = "spike"
		self.rect.left = x
		self.rect.top = y
		self.deadly = True

