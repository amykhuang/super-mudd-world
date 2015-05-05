import pygame
from Background import Background as bg

class Player(pygame.sprite.Sprite):
	STANDING = 0
	JUMPING = 1

	GRAVITY = 1000
	FRICTION = 1000

	def __init__(self):
		#loading images
		self.imageR = pygame.image.load('spear1.png').convert()
		self.imageL = pygame.image.load('spear1L.png').convert()
		self.height = self.imageR.get_height()
		self.width = self.imageR.get_width()

		self.default_image = self.imageR
		self.state = Player.STANDING
		self.move_sound = pygame.mixer.Sound('smb_jumpsmall.wav')

		self.rect = self.imageR.get_rect()

		#position
		self.rect.x = 0
		self.rect.y = bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN

		#velocity
		self.vel = [0,0]
		
		#making white parts black
		self.imageR.set_colorkey((255,255,255))
		self.imageL.set_colorkey((255,255,255))

	def getEvent(self, pressed, background, collides):
		if pressed[pygame.K_UP] and self.state == Player.STANDING and "top" not in collides:
			self.jump()
			self.state = Player.JUMPING

		#if pressed[pygame.K_DOWN]: y += 3

		if pressed[pygame.K_LEFT] and self.rect.x > 0 and "left" not in collides:
			self.default_image = self.imageL
			if self.rect.x < 200 or background.rect.x > -10:
				self.go_left()
			elif background.rect.x < 200: 
				background.shift_world(self.vel[0])

		if pressed[pygame.K_RIGHT] and self.rect.x < 900 and "right" not in collides:
			self.default_image = self.imageR
			if self.rect.x < 200:
				self.go_right()
			elif background.rect.x > bg.SCREEN_WIDTH - background.width:
				background.shift_world(-self.vel[0])
			#self.move_sound.play()

	def gravity(self, dt):
		if self.rect.y < bg.SCREEN_HEIGHT:
			self.vel[1] += Player.GRAVITY * dt
		if self.rect.y >= bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN:
			self.vel[1] = 0
			self.state = Player.STANDING
		if self.vel[0] > 0:
			self.vel[0] -= Player.FRICTION * dt
		if self.vel[0] < 0:
			self.vel[0] += Player.FRICTION * dt

	def blit(self, screen):
		screen.blit(self.default_image, [self.rect.x, self.rect.y])

	def update(self, dt, backgrond, collides):
		if "top" in collides:
			self.vel[1] = 0

		#update positions
		self.rect.x += self.vel[0]*dt
		self.rect.y += self.vel[1]*dt

		#call gravity
		self.gravity(dt)


	def jump(self):
		self.vel[1] -= 500

		if self.rect.y >= 395:
			self.vel[1] = 0

	def go_left(self):
		self.vel[0] -= 50

	def go_right(self):
		self.vel[0] += 50

