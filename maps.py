import pygame
import resources as R
from tiles import *
from enemy import Enemy
from objects import Object
from friend import Friend, TextBox

class Map(pygame.sprite.Sprite):	
	def __init__(self):
		self.platforms = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.objects = pygame.sprite.Group()
		self.friends = pygame.sprite.Group()
		self.textboxes = pygame.sprite.Group()
		self.vel = [0,0]

	def make_map(self, map_array, level):
		""" iterate through map arrays to set platforms, objects, etc.
		"""
		for i in range(len(map_array)):			# iterate through rows
			for j in range(len(map_array[i])):	# iterate through columns
				n = map_array[i][j]				# type of tile
				if n == 1:		# invisible platform
					self.platforms.add(Ground(j*64,i*64))
				if n == 2:		# normal platform
					self.platforms.add(Platform(j*64,i*64))
				if n == 3:		# spike platform
					self.platforms.add(Spike(j*64,i*64))
				if n == 'w':	# wart
					self.enemies.add(Enemy(j*64,i*64,'wart'))
				if n == 'c': 	# cup
					self.objects.add(Object(j*64,i*64,'cup'))
				if n == 'g': 	# glass
					self.objects.add(Object(j*64,i*64,'glass'))
				if n == 'R': 	# Ron
					self.friends.add(Friend(j*64,i*64,'ron'))

	def blit(self, screen, dt):
		title = R.FONTS['Fipps Medium'].render(self.title, True, (0,0,0))

		screen.blit(self.image, [self.rect.left, self.rect.top])
		screen.blit(title, (2,0))
		self.platforms.draw(screen)
		self.enemies.draw(screen)
		self.objects.draw(screen)
		self.friends.draw(screen)

		#update enemy positions
		self.enemies.update(self.rect.left)

		#update textboxes
		self.friends.update(screen)

	def shift_world(self, shift):
		""" moves the background objects as the player moves
		"""
		self.rect.left -= shift
		for platform in self.platforms:
			platform.rect.left -= shift
		for enemy in self.enemies:
		 	enemy.rect.left -= shift
		for thing in self.objects:
		 	thing.rect.left -= shift
		for thing in self.friends:
			thing.rect.left -= shift

class Map00(Map):
	def __init__(self):
		Map.__init__(self)
		self.title = "Linde"
		self.level = 0
		self.image = R.TMX['Map00.png']
		self.make_map(R.MAPS[0], self.level)
		
		self.rect = self.image.get_rect()
		self.rect.left = 0
		self.rect.top = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()

class Endscreen(Map):
	""" the game over screen
		asks if the player would like to play again or exit
	"""
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

