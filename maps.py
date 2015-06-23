import pygame
import pytmx
import resources as R
from tiles import *
from enemy import Enemy

class Map():
	def __init__(self):
		self.platforms = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()

		#position and velocity
		self.rect.x = 0
		self.rect.y = 0
		self.vel = [0,0]

	def make_map(self, level):
		for i in range(len(R.MAPS[level])):	#iterate through rows
			for j in range(len(R.MAPS[level][i])):	#iterate through columns
				n = R.MAPS[level][i][j]	#type of tile
				if n == 1:	#platform
					self.platforms.add(Platform(j*64,i*64))

	#writing to the screen
	def blit(self, screen, dt):
		screen.blit(self.image, [self.rect.x, self.rect.y])	#background image
		text = R.FONTS['Fipps Medium'].render(self.title, True, (0,0,0))
		screen.blit(text, (2,0))	#title
		self.platforms.draw(screen)	#platforms
		self.enemies.draw(screen)	#enemies

		#update enemy positions
		self.enemies.update(dt, self.rect.x)

	def make_Enemies(self):
		#add a for loop
		self.enemies.add(Enemy(450, 'box'))

	def shift_world(self, shift):
		self.rect.x -= shift
		for platform in self.platforms:
			platform.rect.x -= shift
		for enemy in self.enemies:
			enemy.rect.x -= shift

class Map00(Map):
	def __init__(self):
		Map.__init__(self)
		self.name = "Linde"
		self.image = R.TMX['Map00.png']
		self.map = R.MAPS[0]

		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()
		self.title = "Linde"
		self.level = 0

		self.make_Enemies()
		self.make_map(0)

class Endscreen(Map):
	def __init__(self, screen):
		screen.fill((0,0,0))
		title = R.FONTS['Fipps Medium'].render("Game Over", True, (100,0,0))
		title_rect = title.get_rect()
		title_x = R.SCREEN_WIDTH/2 - title_rect.width/2
		title_y = R.SCREEN_HEIGHT/2 - title_rect.height/2 - 20
		subtitle = R.FONTS['Fipps Small'].render("Press space to play again. Press q to quit.", True, (100,0,0))
		subtitle_rect = subtitle.get_rect()
		subtitle_x = R.SCREEN_WIDTH/2 - subtitle_rect.width/2
		subtitle_y = R.SCREEN_HEIGHT/2 - subtitle_rect.height/2 + 70

		screen.blit(title, [title_x, title_y])
		screen.blit(subtitle, [subtitle_x, subtitle_y])

