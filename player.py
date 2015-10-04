import pygame
import resources as R

class Player(pygame.sprite.Sprite):

	def __init__(self):
		# loading images
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
		self.damage_time = 0	# once damaged, is immune for a bit
		self.on_enemy = False	# if standing on top of enemy, no damage
		self.talking = False	# whether it is talking to a friend

		# position and velocity
		self.rect.left = 0
		self.rect.top = 300
		self.vel = [0,0]

		# rect for collisions 
		self.collideRect = pygame.rect.Rect((0,0), (32,150))
		self.collideRect.left = self.rect.left
		self.collideRect.top = self.rect.top

	def blit(self, screen):
		""" writes the following to the screen:
			the player and its health
		"""
		screen.blit(self.default_image, [self.rect.left, self.rect.top])	#self
		health = R.FONTS['Fipps Medium'].render(str(self.health), True, (0,0,0))
		screen.blit(health, [R.SCREEN_WIDTH - health.get_width() - 10, 0])	#health

	def getEvent(self):
		""" reads the keypress, and reacts accordingly
		"""
		pressed = pygame.key.get_pressed() #get keypress

		if pressed[pygame.K_UP] and self.state == "standing":
			self.isjump = True

		if pressed[pygame.K_LEFT] and self.rect.left > 0:
			self.vel[0] = -R.STEP

		if pressed[pygame.K_RIGHT] and self.rect.left < 900:
			self.vel[0] = R.STEP
			# self.move_sound.play()

		#add the speed of what it's standing on
		self.vel[0] += self.platform_speed_x

	def update(self, dt, bg):
		""" update the position of the player, 
		"""
		#get event from keypress
		self.getEvent()

		ticks = pygame.time.get_ticks()	#time elapsed so far

		if self.isjump:	#check if jumping
			self.jump() #jump!
			self.isjump = False
			self.state = "jumping"
			self.platform_speed_x = 0

		# update positions
		dx = self.vel[0]
		dy = self.vel[1] * dt
		
		# move positions
		self.move(dx, 0, bg, dt, ticks)
		self.move(0, dy, bg, dt, ticks)

		self.gravity(dt)
		self.vel[0] = 0

		# change states, if necessary
		if self.health <= 0:
			return "gameover"		#sets game_over to True
		return "in_game"

	def move(self, dx, dy, bg, dt, ticks):
		""" moves the Player or shifts the background. 
			also checks for collisions
		"""
		if self.vel[0] < 0 and self.rect.left > 0:	#move left
			self.walkcycle(ticks)
			if (self.rect.left - bg.rect.left <= 200) or (bg.width + bg.rect.left <= R.SCREEN_WIDTH and self.rect.left > 200):
				self.rect.left += dx
			elif bg.rect.left < 200:
				bg.shift_world(dx)
		if self.vel[0] > 0 and self.rect.left < 900:	#move right
			self.walkcycle(ticks)
			if self.rect.left < 200 or (bg.width + bg.rect.left <= R.SCREEN_WIDTH):
				self.rect.left += dx
			elif bg.rect.left > R.SCREEN_WIDTH - bg.width:
				bg.shift_world(dx)
		self.rect.top += dy

		# COLLISION CHECKING

		# collision checking for platforms
		# only checks for bottom collisions; otherwise goes through platform
		block_hit_list = pygame.sprite.spritecollide(self, bg.platforms, False)
		for block in block_hit_list:
			if self.rect.colliderect(block.rect):
				if dy > 0 and self.rect.bottom <= block.rect.top + 25:
					self.rect.bottom = block.rect.top
					self.vel[1] = 0
					self.state = "standing"
 					self.platform_speed_x = block.vel[0]	#save platform speed

		# collision checking for enemies
		self.on_enemy = False
		block_hit_list = pygame.sprite.spritecollide(self, bg.enemies, False)
		for enemy in block_hit_list:
			if self.rect.colliderect(enemy.rect):
				if dy > 0 and self.rect.bottom < enemy.rect.bottom:
					self.rect.bottom = enemy.rect.top
					self.vel[1] = 0
					self.state = "standing"
					self.on_enemy = True
 					self.platform_speed_x = enemy.vel[0]	#save platform speed
				# if dy < 0:
				# 	self.rect.top = block.rect.bottom
				# 	self.vel[1] = -0.3 * self.vel[1]

				# check for damage and record time
				self.damage_time = self.damage(enemy, ticks)

		# collision checking for objects
		block_hit_list = pygame.sprite.spritecollide(self, bg.objects, False)
		for thing in block_hit_list:
			if self.rect.colliderect(thing.rect):
				# lose health when colliding with damaging objects
				if thing.deadly:
					self.damage_time = self.damage(thing, ticks)
				# gain health when colliding with healthy objects
				elif thing.health:
					self.health += thing.health
					thing.kill()

		# collision checking for other characters
		block_hit_list = pygame.sprite.spritecollide(self, bg.friends, False)
		for friend in block_hit_list:
			if self.rect.colliderect(friend.rect):

				# if it is a speaking friend
				if dx > 0 and friend.speak:
					self.rect.right = friend.rect.left
					self.talking = True
				# if it has finished speaking, do nothing					
	
	def damage(self, block, ticks):
		""" decreases health when running into things
		"""
		#runs into spike platform
		if block.species == "spike" and self.damaged == False:
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

	    # walking to the left
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

	    # walking to the right
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
		self.vel[1] += R.JUMP_VELOCITY

