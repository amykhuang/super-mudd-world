import pygame

class Sprite:
	def __init__(self):
		#loading images
		self.imageR = pygame.image.load('spear1.png').convert()
		self.imageL = pygame.image.load('spear1L.png').convert()
		self.height = self.imageR.get_height()
		self.width = self.imageR.get_width()
		
		#position
		self.x = 0
		self.y = 275
		
		#making white parts black
		self.imageR.set_colorkey((255,255,255))
		self.imageL.set_colorkey((255,255,255))
