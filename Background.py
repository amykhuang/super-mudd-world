import pygame

class Background:

	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 395
	BOTTOM_MARGIN = 20

	def __init__(self):
		#load image
		self.image = pygame.image.load('background-1500.png').convert()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.title = "SUPER MUDD"
		
		#position
		self.x = 0
		self.y = 0

		#text 
		self.font = pygame.font.Font("Fipps-Regular.otf", 30)
		self.text = self.font.render(self.title, True, (0,0,0))
		
