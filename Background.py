import pygame

class Background(pygame.sprite.Sprite):

	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 395
	BOTTOM_MARGIN = 20
	STEP = 3

	def __init__(self):
		#load image
		self.image = pygame.image.load('background-1500.png').convert()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()
		self.title = "SUPER MUDD"

		#adding the platforms
		self.platforms = []
		#might put these positions in a separate file at some point
		self.plat_positions = [
			[100, 300, "platform"],
			[300, 200, "platform"],
			[600, 240, "platform"],
			[200, 360, "spike"]
		]
		self.make_Platforms()
		
		#position and velocity
		self.rect.x = 0
		self.rect.y = 0
		self.vel = [0,0]

		#text 
		self.font = pygame.font.Font("Fipps-Regular.otf", 30)
		self.text = self.font.render(self.title, True, (0,0,0))

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])
		screen.blit(self.text, (0,0))
		for i in self.platforms:
			i.blit(screen)

	def make_Platforms(self):
		self.platforms += [Platform(0, Background.SCREEN_HEIGHT-Background.BOTTOM_MARGIN, "ground")]
		for i in self.plat_positions:
			new_plat = Platform(i[0],i[1],i[2])
			self.platforms += [new_plat]

	def shift_world(self, shift):
		self.rect.left -= shift
		for platform in self.platforms:
			platform.rect.left -= shift

class Platform:
	def __init__(self, x, y, typ):
		if typ == "platform":
			self.image = pygame.image.load('redplat.png').convert()
		elif typ == "spike":
			self.image = pygame.image.load('spikeplat.png').convert()
		else:
			self.image = pygame.image.load('ground.png').convert_alpha()

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.vel = [0,0]
		self.type = typ


	def blit(self, screen):
		screen.blit(self.image, [self.rect.left, self.rect.top])
