import pygame
from Background import Background as bg
import resources as R

class Player(pygame.sprite.Sprite):

	def __init__(self):
		#loading images
		self.default_image = R.IMAGES["exbig1.png"]

		self.height = self.default_image.get_height()
		self.width = self.default_image.get_width()
		self.rect = self.default_image.get_rect()

		self.move_sound = R.SOUNDS['smb_jumpsmall.wav']

		self.state = "standing"
		self.isjump = False
		self.health = 10
		self.damaged = False
		self.damage_time = 0

		#position and velocity
		self.rect.x = 0
		self.rect.y = R.SCREEN_HEIGHT - self.height - R.BOTTOM_MARGIN
		self.vel = [0,0]

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.default_image, [self.rect.x, self.rect.y])	#self

		health = R.FONTS['Fipps-Regular.otf'].render(str(self.health), True, (0,0,0))
		screen.blit(health, [R.SCREEN_WIDTH - health.get_width() - 10, 0])	#health

	def getEvent(self):
		""" reads the keypress
		"""
		pressed = pygame.key.get_pressed() #get keypress

		if pressed[pygame.K_UP] and self.state == "standing":
			self.isjump = True

		if pressed[pygame.K_LEFT] and self.rect.x > 0:
			self.vel[0] = -R.STEP #amount to travel left

		if pressed[pygame.K_RIGHT] and self.rect.x < 900:
			self.vel[0] = R.STEP
			#self.move_sound.play()

	def update(self, dt, bg):
		#get event from keypress
		self.getEvent()

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
		self.move(dx, 0, bg, dt, ticks)
		self.move(0, dy, bg, dt, ticks)

		self.gravity(dt)
		self.vel[0] = 0

		if self.health <= 0:
			return "gameover"		#sets game_over to True
		return "in_game"

	def move(self, dx, dy, bg, dt, ticks):
		""" moves the Player
		"""
		if self.vel[0] < 0 and self.rect.x > 0:	#move left
			self.walkcycle("left", ticks)
			if self.rect.x < 200 or bg.rect.x > -10:
				self.rect.left += dx
			elif bg.rect.x < 200:
				bg.shift_world(dx)
		if self.vel[0] > 0 and self.rect.x < 900:	#move right
			self.walkcycle("right", ticks)
			if self.rect.x < 200:
				self.rect.left += dx
			elif bg.rect.x > R.SCREEN_WIDTH - bg.width:
				bg.shift_world(dx)
		self.rect.y += dy

		# checking for collisions
		block_hit_list = pygame.sprite.spritecollide(self, bg.platforms, False)
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
	    		self.default_image = R.IMAGES["spear1L.png"].convert()
	    	elif ticks % 30 <= 20 and ticks % 30 > 10:
	    		self.default_image = R.IMAGES["spear1L.png"].convert()
	    	else:
	    		self.default_image = R.IMAGES["spear1L.png"].convert()
	    elif direction == "right":
	    	if ticks % 30 <= 10:
	    		self.default_image = R.IMAGES["exbig1.png"].convert()
	    	elif ticks % 30 <= 20 and ticks % 30 > 10:
	    		self.default_image = R.IMAGES["exbig2.png"].convert()
	    	else:
	    		self.default_image = R.IMAGES["exbig3.png"].convert()


	def gravity(self, dt):
		self.vel[1] += R.GRAVITY * dt

	def jump(self):
		self.vel[1] -= 500

