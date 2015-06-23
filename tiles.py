import pygame
import resources as R

class Tile(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = R.IMAGES['tile.png']
		self.rect = self.image.get_rect()
		self.vel = [0,0]

class Platform(Tile):
	def __init__(self, x, y):
		Tile.__init__(self, x, y)
		self.type = "platform"
		self.rect.x = x
		self.rect.y = y

class Spike(Tile):
	def __init__(self, x, y):
		Tile.__init__(self, x, y)
		self.type = "spike"
		self.rect.x = x
		self.rect.y = y

