import pygame
import resources as R

class Enemy(pygame.sprite.DirtySprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		types = {
			'wart': [R.IMAGES["wart1L.png"], 100, 3]
		}

		self.image = types[typ][0]
		self.start = x
		self.end = self.start + types[typ][1]	#distance that it walks

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		
		#position and velocity
		self.rect.x = x
		self.rect.y = y + 64 - self.height
		self.step = types[typ][2]
		self.vel = [self.step, 0]

		self.type = "enemy"
		self.species = "wart"
		self.dead = False
		self.dirty = 1

	def update(self, dt, bg_pos):
		""" update the position of the enemy
			so that it moves back and forth
		"""
		ticks = pygame.time.get_ticks()
		self.walkcycle(ticks)

		#turn around on reaching limits
		if self.rect.x >= self.end + bg_pos:
			self.vel[0] = -self.step
		elif self.rect.x < self.start + bg_pos:
			self.vel[0] = self.step

		#update positions
		dx = self.vel[0]
		self.rect.x += dx

	def walkcycle(self, ticks):
		n = ticks % 800
		cycles = {
			"wart": [R.IMAGES["wart1L.png"], R.IMAGES["wart2L.png"], R.IMAGES["wart3L.png"], R.IMAGES["wart1R.png"], R.IMAGES["wart2R.png"], R.IMAGES["wart3R.png"]]
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

