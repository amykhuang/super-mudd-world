import pygame
from Background import Background as bg

WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
	GRAVITY = 1000

	def __init__(self):
		#loading images
		self.imageR = pygame.image.load('images/spear1.png').convert()
		self.imageR1 = pygame.image.load('images/exbig1.png').convert()
		self.imageR2 = pygame.image.load('images/exbig2.png').convert()
		self.imageR3 = pygame.image.load('images/exbig3.png').convert()
		self.imageL = pygame.image.load('images/spear1L.png').convert()
		self.default_image = self.imageR1

		player_images = [self.imageR, self.imageR1, self.imageR2, self.imageR3, self.imageL]

		self.height = self.imageR.get_height()
		self.width = self.imageR.get_width()
		self.rect = self.imageR.get_rect()

		self.move_sound = pygame.mixer.Sound('sounds/smb_jumpsmall.wav')
		self.font = pygame.font.Font("Fipps-Regular.otf", 30)

		self.state = "standing"
		self.isjump = False
		self.health = 10
		self.damaged = False
		self.damage_time = 0

		#position
		self.rect.x = 0
		self.rect.y = bg.SCREEN_HEIGHT - self.height - bg.BOTTOM_MARGIN
		#velocity
		self.vel = [0,0]
		
		#making white parts black
		for image in player_images:
			image.set_colorkey(WHITE)

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.default_image, [self.rect.x, self.rect.y])	#self

		health = self.font.render(str(self.health), True, (0,0,0))
		screen.blit(health, [bg.SCREEN_WIDTH-health.get_width()-10,0])	#health

	def getEvent(self, background):
		""" reads the keypress
		"""
		pressed = pygame.key.get_pressed() #get keypress

		if pressed[pygame.K_UP] and self.state == "standing":
			self.isjump = True

		if pressed[pygame.K_LEFT] and self.rect.x > 0:
			self.vel[0] = -bg.STEP #amount to travel left

		if pressed[pygame.K_RIGHT] and self.rect.x < 900:
			self.vel[0] = bg.STEP
			#self.move_sound.play()

	def update(self, dt, background):
		#get event from keypress
		self.getEvent(background)

		ticks = pygame.time.get_ticks()	#time elapsed so far

		#check if jumping
		if self.isjump:	#jump!
			self.jump()
			self.isjump = False
			self.state = "jumping"

		#update positions
		dx = self.vel[0]
		dy = self.vel[1] * dt
		
		#collides, kill = background.collision_check_h(self)
		self.move(dx, 0, background, dt, ticks)
		self.move(0, dy, background, dt, ticks)

		self.gravity(dt)
		self.vel[0] = 0

		if self.health <= 0:
			return "gameover"		#sets game_over to True
		return "in_game"

	def move(self, dx, dy, background, dt, ticks):
		""" moves the Player
		"""
		if self.vel[0] < 0 and self.rect.x > 0:	#move left
			self.walkcycle("left", ticks)
			if self.rect.x < 200 or background.rect.x > -10:
				self.rect.left += dx
			elif background.rect.x < 200:
				background.shift_world(dx)
		if self.vel[0] > 0 and self.rect.x < 900:	#move right
			self.walkcycle("right", ticks)
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
					self.vel[1] = -0.3 * self.vel[1]	#bouncing off
				self.damage_time = self.damage(block, ticks)	#checking for damage
	
	def damage(self, block, ticks):
		""" decreases health when running into things
		"""
		if block.type == "spike" and self.damaged == False:
			self.health -= 1
			self.damaged = True
			return ticks
		else:
			if ticks - self.damage_time > 300:
				self.damaged = False
			return self.damage_time

	def walkcycle(self, direction, ticks):
	    """ creates the walking animation
	    """
	    if direction == "left":
	    	if ticks % 30 <= 10:
	    		self.default_image = self.imageL
	    	elif ticks % 30 <= 20 and ticks % 30 > 10:
	    		self.default_image = self.imageL
	    	else:
	    		self.default_image = self.imageL
	    elif direction == "right":
	    	if ticks % 30 <= 10:
	    		self.default_image = self.imageR1
	    	elif ticks % 30 <= 20 and ticks % 30 > 10:
	    		self.default_image = self.imageR2
	    	else:
	    		self.default_image = self.imageR3


	def gravity(self, dt):
		self.vel[1] += Player.GRAVITY * dt

	def jump(self):
		self.vel[1] -= 500

