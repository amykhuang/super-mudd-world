import pygame

class Background:
	def __init__(self):
		#load image
		self.image = pygame.image.load('background2.png').convert()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		
		#position
		self.x = 0
		self.y = 0
