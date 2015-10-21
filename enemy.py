import pygame
import resources as R

class Enemy(pygame.sprite.DirtySprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		# [image, walkdistance, stepsize, health]
		enemy_dict = {	
			'wart': [R.IMAGES["wart1L.png"], 100, 3, 3]
		}

		self.image = enemy_dict[typ][0]
		self.start = x
		self.end = self.start + enemy_dict[typ][1]	# its walking range

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		
		#position and velocity
		self.rect.left = x
		self.rect.top = y + 64 - self.height
		self.step = enemy_dict[typ][2]
		self.vel = [self.step, 0]

		self.species = "wart"
		self.dead = False
		self.deadly = True
		self.health = enemy_dict[typ][2]
		self.dirty = 1

	def update(self, bg_pos):
		""" update the position of the enemy
			so that it moves back and forth
		"""
		ticks = pygame.time.get_ticks()
		self.walkcycle(ticks)

		#turn around on reaching limits
		if self.rect.left >= self.end + bg_pos:
			self.vel[0] = -self.step
		elif self.rect.left < self.start + bg_pos:
			self.vel[0] = self.step

		#update positions
		dx = self.vel[0]
		self.rect.left += dx

	def walkcycle(self, ticks):
		n = ticks % 800

		# walkcycles for other objects
		cycles = {
			"wart": [R.IMAGES["wart1L.png"], R.IMAGES["wart2L.png"],\
			R.IMAGES["wart3L.png"], R.IMAGES["wart1R.png"], R.IMAGES["wart2R.png"],\
			R.IMAGES["wart3R.png"]]
		}
		if self.vel[0] < 0:
			if n <= 200:
				self.image = cycles[self.species][0]
			elif n <= 400 and n > 200:
				self.image = cycles[self.species][1]
			elif n <= 600 and n > 400:
				self.image = cycles[self.species][2]
			else:
				self.image = cycles[self.species][1]
		elif self.vel[0] >= 0:
			if n <= 200:
				self.image = cycles[self.species][3]
			elif n <= 400 and n > 200:
				self.image = cycles[self.species][4]
			elif n <= 600 and n > 400:
				self.image = cycles[self.species][5]
			else:
				self.image = cycles[self.species][4]

