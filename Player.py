import pygame
from Background import Background as bg

class Player(pygame.sprite.Sprite):
	STANDING = 0
	JUMPING = 1

	GRAVITY = 1000

	def __init__(self):
		#loading images
		self.imageR = pygame.image.load('spear1.png').convert()
		self.imageL = pygame.image.load('spear1L.png').convert()
		self.height = self.imageR.get_height()
		self.width = self.imageR.get_width()
		self.default_image = self.imageR
		self.state = Player.STANDING
		self.move_sound = pygame.mixer.Sound('smb_jumpsmall.wav')

		
		#position
		self.x = 0
		self.y = bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN

		#velocity
		self.vel = [0,0]
		
		#making white parts black
		self.imageR.set_colorkey((255,255,255))
		self.imageL.set_colorkey((255,255,255))

	def get_rect(self):
		return pygame.Rect([self.x, self.y],[self.width, self.height])

	def keyPress(self, pressed, background, collides):
		if pressed[pygame.K_UP] and self.state == Player.STANDING and "top" not in collides:
			self.jump(collides)
			self.state = Player.JUMPING

		#if pressed[pygame.K_DOWN]: y += 3

		if pressed[pygame.K_LEFT] and self.x > 0 and "left" not in collides:
			self.default_image = self.imageL
			if self.x < 200 or background.x > -200:
				self.x -= 3
			elif background.x < 200: 
				background.x += 3

		if pressed[pygame.K_RIGHT] and self.x < 900 and "right" not in collides:
			self.default_image = self.imageR
			if self.x < 200:
				self.x += 3
			elif background.x > bg.SCREEN_WIDTH - background.width:
				background.x -= 3
			#self.move_sound.play()

	def update(self, dt, collides):
		if "top" in collides:
			self.vel[1] = 0
		self.x += self.vel[0]*dt
		self.y += self.vel[1]*dt

		if self.y < bg.SCREEN_HEIGHT:
			self.vel[1] += Player.GRAVITY * dt

		if self.y >= bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN:
			self.vel[1] = 0
			self.state = Player.STANDING


	def jump(self, collides):
		self.vel[1] -= 500


		if self.y >= 395:
			self.vel[1] = 0

