import pygame
from Background import Background as bg

class Player(pygame.sprite.Sprite):
	STANDING = "standing"
	JUMPING = "jumping"

	GRAVITY = 1000

	def __init__(self):
		#loading images
		self.imageR = pygame.image.load('spear1.png').convert()
		self.imageL = pygame.image.load('spear1L.png').convert()
		self.height = self.imageR.get_height()
		self.width = self.imageR.get_width()

		self.default_image = self.imageR
		self.state = "standing"
		self.move_sound = pygame.mixer.Sound('smb_jumpsmall.wav')
		self.isjump = False

		self.rect = self.imageR.get_rect()

		#position
		self.rect.x = 0
		self.rect.y = bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN

		#velocity
		self.vel = [0,0]
		
		#making white parts black
		self.imageR.set_colorkey((255,255,255))
		self.imageL.set_colorkey((255,255,255))

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.default_image, [self.rect.x, self.rect.y])

	def getEvent(self, background):
		pressed = pygame.key.get_pressed() #get keypress

		if pressed[pygame.K_UP] and self.state == Player.STANDING:
			self.isjump = True

		if pressed[pygame.K_LEFT] and self.rect.x > 0:
			self.vel[0] = -bg.STEP #amount to travel left

		if pressed[pygame.K_RIGHT] and self.rect.x < 900:
			self.vel[0] = bg.STEP
			#self.move_sound.play()

	def gravity(self, dt):
		self.vel[1] += Player.GRAVITY * dt

	def update(self, dt, background):
		#get event from keypress
		self.getEvent(background)

		#check if jumping
		if self.isjump:	#jump!
			self.jump()
			self.isjump = False
			self.state = "jumping"

		#update positions
		dx = self.vel[0]
		dy = self.vel[1] * dt
		
		#collides, kill = background.collision_check_h(self)
		self.move(dx, 0, background, dt)
		self.move(0, dy, background, dt)

		self.gravity(dt)
		self.vel[0] = 0

	def move(self, dx, dy, background, dt):
		# move the rect
		if self.vel[0] < 0 and self.rect.x > 0:	#move lieft
			self.default_image = self.imageL
			if self.rect.x < 200 or background.rect.x > -10:
				self.rect.left += dx
			elif background.rect.x < 200:
				background.shift_world(dx)
		if self.vel[0] > 0 and self.rect.x < 900:	#move right
			self.default_image = self.imageR
			if self.rect.x < 200:
				self.rect.left += dx
			elif background.rect.x > bg.SCREEN_WIDTH - background.width:
				background.shift_world(dx)
		self.rect.y += dy

		# checking for collisions
		block_hit_list = pygame.sprite.spritecollide(self, background.platforms, False)
		for block in block_hit_list:
			if self.rect.colliderect(block.rect):
				if dx > 0:
					self.rect.right = block.rect.left
				if dx < 0:
					self.rect.left = block.rect.right
				if dy > 0:
					self.rect.bottom = block.rect.top
					self.vel[1] = 0
					self.state = "standing"
				if dy < 0:
					self.rect.top = block.rect.bottom
					self.gravity(dt)

	def jump(self):
		self.vel[1] -= 500

