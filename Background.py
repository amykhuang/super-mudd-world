import pygame

class Background(pygame.sprite.Sprite):

	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 395
	BOTTOM_MARGIN = 20
	STEP = 3

	def __init__(self):
		#load image
		self.image = pygame.image.load('images/background-1500.png').convert()
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
		self.smallfont = pygame.font.Font("Fipps-Regular.otf", 20)
		self.text = self.font.render(self.title, True, (0,0,0))

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])
		screen.blit(self.text, (0,0))
		for i in self.platforms:
			i.blit(screen)

	def endscreen(self, screen):
		screen.fill((0,0,0))
		title = self.font.render("Game Over", True, (100,0,0))
		title_rect = title.get_rect()
		title_x = screen.get_width()/2 - title_rect.width/2
		title_y = screen.get_height()/2 - title_rect.height/2 - 20
		subtitle = self.smallfont.render("Press space to play again. Press q to quit.", True, (100,0,0))
		subtitle_rect = subtitle.get_rect()
		subtitle_x = screen.get_width()/2 - subtitle_rect.width/2
		subtitle_y = screen.get_height()/2 - subtitle_rect.height/2 + 70

		screen.blit(title, [title_x, title_y])
		screen.blit(subtitle, [subtitle_x, subtitle_y])


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
			self.image = pygame.image.load('images/redplat.png').convert()
		elif typ == "spike":
			self.image = pygame.image.load('images/spikeplat.png').convert()
		else:
			self.image = pygame.image.load('images/ground.png').convert_alpha()

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.vel = [0,0]
		self.type = typ


	def blit(self, screen):
		screen.blit(self.image, [self.rect.left, self.rect.top])
