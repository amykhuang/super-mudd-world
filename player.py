import pygame
import resources as R

class Player(pygame.sprite.Sprite):

	def __init__(self):
		#loading images
		self.default_image = R.IMAGES["walkR1.png"]

		self.height = self.default_image.get_height()
		self.width = self.default_image.get_width()
		self.rect = self.default_image.get_rect()

		self.move_sound = R.SOUNDS['smb_jumpsmall.wav']

		self.state = "start"
		self.isjump = False
		self.platform_speed_x = 0
		self.health = 10
		self.damaged = False
		self.damage_time = 0
		self.on_enemy = False	#check if standing on top of enemy

		#position and velocity
		self.rect.x = 0
		self.rect.y = 300
		self.vel = [0,0]

	#writing to the screen
	def blit(self, screen):
		screen.blit(self.default_image, [self.rect.x, self.rect.y])	#self
		health = R.FONTS['Fipps Medium'].render(str(self.health), True, (0,0,0))
		screen.blit(health, [R.SCREEN_WIDTH - health.get_width() - 10, 0])	#health

	def getEvent(self):
		""" reads the keypress
		"""
		pressed = pygame.key.get_pressed() #get keypress

		if pressed[pygame.K_UP] and self.state == "standing":
			self.isjump = True

		if pressed[pygame.K_LEFT] and self.rect.x > 0:
			self.vel[0] = -R.STEP

		if pressed[pygame.K_RIGHT] and self.rect.x < 900:
			self.vel[0] = R.STEP
			#self.move_sound.play()

		self.vel[0] += self.platform_speed_x	#add the speed of what it's standing on

	def update(self, dt, bg):
		#get event from keypress
		self.getEvent()

		ticks = pygame.time.get_ticks()	#time elapsed so far

		if self.isjump:	#check if jumping
			self.jump() #jump!
			self.isjump = False
			self.state = "jumping"
			self.platform_speed_x = 0

		#update positions
		dx = self.vel[0]
		dy = self.vel[1] * dt
		
		#move positions
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
			self.walkcycle(ticks)
			if self.rect.x - bg.rect.x <= 200 or bg.rect.x > 0:
				self.rect.left += dx
			elif bg.rect.x < 200:
				bg.shift_world(dx)
		if self.vel[0] > 0 and self.rect.x < 900:	#move right
			self.walkcycle(ticks)
			if self.rect.x < 200:
				self.rect.left += dx
			elif bg.rect.x > R.SCREEN_WIDTH - bg.image.get_width():
				bg.shift_world(dx)
		self.rect.y += dy

		# collision checking
		self.on_enemy = False
		block_hit_list = pygame.sprite.spritecollide(self, bg.platforms, False)
		block_hit_list += pygame.sprite.spritecollide(self, bg.enemies, False)
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
					self.on_enemy = True
 					self.platform_speed_x = block.vel[0]	#save the speed of platform
				if dy < 0:
					self.rect.top = block.rect.bottom
					self.vel[1] = -0.3 * self.vel[1]	#bouncing off
				self.damage_time = self.damage(block, ticks)	#checking for damage

		# collision checking for objects
		object_hit_list = pygame.sprite.spritecollide(self, bg.objects, False)
		for thing in object_hit_list:
			if self.rect.colliderect(thing.rect):
				if thing.deadly == True:
					self.damage_time = self.damage(thing, ticks)
	
	def damage(self, block, ticks):
		""" decreases health when running into things
		"""
		#runs into spike platform
		if block.type == "spike" and self.damaged == False:
			self.health -= 1
			self.damaged = True
			return ticks
		#runs into enemy
		elif block.deadly == True and self.on_enemy == False and self.damaged == False:
			self.health -= 1
			self.damaged = True
			return ticks
		else:
			if ticks - self.damage_time > 300:
				self.damaged = False
			return self.damage_time

	def walkcycle(self, ticks):
	    """ creates the walking animation
	    """
	    n = ticks % 800
	    if self.vel[0] < 0:
	    	if self.state == "jumping":
	    		self.default_image = R.IMAGES["walkL2.png"]
	    	elif n <= 200:
	    		self.default_image = R.IMAGES["walkL1.png"]
	    	elif n <= 400 and n > 200:
	    		self.default_image = R.IMAGES["walkL2.png"]
	    	elif n <= 600 and n > 400:
	    		self.default_image = R.IMAGES["walkL3.png"]
	    	else:
	    		self.default_image = R.IMAGES["walkL2.png"]
	    elif self.vel[0] >= 0:
	    	if self.state == "jumping":
	    		self.default_image = R.IMAGES["walkR2.png"]
	    	elif n <= 200:
	    		self.default_image = R.IMAGES["walkR1.png"]
	    	elif n <= 400 and n > 200:
	    		self.default_image = R.IMAGES["walkR2.png"]
	    	elif n <= 600 and n > 400:
	    		self.default_image = R.IMAGES["walkR3.png"]
	    	else:
	    		self.default_image = R.IMAGES["walkR2.png"]


	def gravity(self, dt):
		self.vel[1] += R.GRAVITY * dt

	def jump(self):
		self.vel[1] -= 500

