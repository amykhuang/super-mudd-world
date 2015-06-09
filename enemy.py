import pygame
import resources as R

class Enemy(pygame.sprite.DirtySprite):

	def __init__(self, start, typ):
		pygame.sprite.Sprite.__init__(self)

		types = {
			'box': [R.IMAGES["enemy1.png"], 100, 100]
		}

		self.image = types[typ][0]
		self.start = start
		self.end = self.start + types[typ][1]	#distance that it walks

		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = self.image.get_rect()
		
		#position and velocity
		self.rect.x = start
		self.rect.y = R.SCREEN_HEIGHT - self.height - R.BOTTOM_MARGIN
		self.speed = types[typ][2]
		self.vel = self.speed

		self.dead = False


	def update(self, dt):
		ticks = pygame.time.get_ticks()	#time elapsed so far

		#turn around on reaching limits
		if self.rect.x >= self.end:
			self.vel = -self.speed
		elif self.rect.x < self.start:
			self.vel = self.speed

		#update positions
		dx = self.vel * dt
		self.rect.x += dx

	def walkcycle(self, ticks):
		n = ticks % 800

