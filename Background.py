import pygame
import resources as R

class Background(pygame.sprite.Sprite):

	def __init__(self):
		#load image
		self.image = R.IMAGES['background-1500.png'].convert()
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
		self.smallfont = pygame.font.Font("data/fonts/Fipps-Regular.otf", 20)
		self.text = R.FONTS['Fipps-Regular.otf'].render(self.title, True, (0,0,0))

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])
		screen.blit(self.text, (2,0))
		for i in self.platforms:
			i.blit(screen)

	def endscreen(self, screen):
		screen.fill((0,0,0))
		title = R.FONTS['Fipps-Regular.otf'].render("Game Over", True, (100,0,0))
		title_rect = title.get_rect()
		title_x = R.SCREEN_HEIGHT/2 - title_rect.width/2
		title_y = R.SCREEN_HEIGHT/2 - title_rect.height/2 - 20
		subtitle = self.smallfont.render("Press space to play again. Press q to quit.", True, (100,0,0))
		subtitle_rect = subtitle.get_rect()
		subtitle_x = R.SCREEN_WIDTH/2 - subtitle_rect.width/2
		subtitle_y = R.SCREEN_WIDTH/2 - subtitle_rect.height/2 + 70

		screen.blit(title, [title_x, title_y])
		screen.blit(subtitle, [subtitle_x, subtitle_y])


	def make_Platforms(self):
		self.platforms += [Platform(0, R.SCREEN_HEIGHT-R.BOTTOM_MARGIN, "ground")]
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
			self.image = R.IMAGES['redplat.png']
		elif typ == "spike":
			self.image = R.IMAGES['spikeplat.png']
		else:
			self.image = R.IMAGES['ground.png']

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y
		self.vel = [0,0]
		self.type = typ


	def blit(self, screen):
		screen.blit(self.image, [self.rect.left, self.rect.top])
