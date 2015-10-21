import pygame
from friend import TextBox
import resources as R

class Player(pygame.sprite.Sprite):

	def __init__(self):

		self.default_image = R.IMAGES["walkR1.png"]

		self.height = self.default_image.get_height()
		self.width = self.default_image.get_width()
		self.rect = self.default_image.get_rect()

		# States include: start, standing, jumping
		self.state = "start"

		# State variables
		self.health = 10
		self.walking = False	# if not walking, don't do walkcycle images
		self.platform_speed_x = 0
		self.damaged = False	
		self.damage_time = 0	# once damaged, is immune for a bit

		# Position and velocity
		self.rect.left = 0
		self.rect.top = 300
		self.vel = [0,0]

		# Rect for collisions (does not yet work)
		self.collideRect = pygame.rect.Rect((0,0), (32,150))
		self.collideRect.left = self.rect.left
		self.collideRect.top = self.rect.top

		self.textbox = None


	def blit(self, screen):
		""" writes the following to the screen:
			the player and its health
		"""
		screen.blit(self.default_image, [self.rect.left, self.rect.top])	#self
		health = R.FONTS['Fipps Medium'].render(str(self.health), True, (0,0,0))
		screen.blit(health, [R.SCREEN_WIDTH - health.get_width() - 10, 0])	#health

		if self.textbox:
			screen.blit(self.textbox.image, (self.textbox.x_pos, self.textbox.y_pos))


	def update(self, dt, bg, keypress):
		""" update the position of the player, 
		"""
		ticks = pygame.time.get_ticks()	# time elapsed so far

		self.getEvent(bg, keypress)		# respond to the keypress

		# Update positions
		dx = self.vel[0]
		dy = self.vel[1] * dt
		
		self.move(dx, 0, bg, dt, ticks)
		self.move(0, dy, bg, dt, ticks)

		self.vel[1] += R.GRAVITY * dt 	# gravity
		self.vel[0] = 0

		# Change the game state, if necessary
		if self.health <= 0:
			return "gameover"
		if self.state == "speaking": 
			return "speaking"
		return "in_game"


	def getEvent(self, bg, keypress):
		""" gets the keypress, and reacts accordingly
		"""
		self.walking = False

		# Jump
		if keypress[pygame.K_UP] and self.state == "standing":
			self.vel[1] += R.JUMP_VELOCITY
			self.state = "jumping"
			self.platform_speed_x = 0
			# R.SOUNDS['smb_jumpsmall.wav'].play()

		# Step to left
		if keypress[pygame.K_LEFT] and self.rect.left > 0:
			self.vel[0] = -R.STEP
			self.walking = True

		# Step to right
		if keypress[pygame.K_RIGHT] and self.rect.left < 900:
			self.vel[0] = R.STEP
			self.walking = True

		friends = pygame.sprite.spritecollide(self, bg.friends, False)
		if keypress[pygame.K_SPACE] and friends:
			self.textbox = friends[0].show_text()
			self.state = "speaking"

		# Add the speed of what it's standing on
		self.vel[0] += self.platform_speed_x


	def move(self, dx, dy, bg, dt, ticks):
		""" moves the Player or shifts the background. 
			also checks for collisions
		"""
		if self.vel[0] < 0 and self.rect.left > 0:	#move left
			if (self.rect.left - bg.rect.left <= 200) \
			or (bg.width + bg.rect.left <= R.SCREEN_WIDTH \
				and self.rect.left > 200):
				self.rect.left += dx
			elif bg.rect.left < 200:
				bg.shift_world(dx)
		if self.vel[0] > 0 and self.rect.left < 900:	#move right
			if self.rect.left < 200 or (bg.width + bg.rect.left <= R.SCREEN_WIDTH):
				self.rect.left += dx
			elif bg.rect.left > R.SCREEN_WIDTH - bg.width:
				bg.shift_world(dx)
		self.rect.top += dy 	# gravity

		self.update_image(ticks)


		### collision checking

		# collision checking for platforms
		# can jump through platforms
		block_hit_list = pygame.sprite.spritecollide(self, bg.platforms, False)
		for block in block_hit_list:
			if self.rect.colliderect(block.rect):
				if dy > 0 and self.rect.bottom <= block.rect.top + 25:
					self.rect.bottom = block.rect.top
					self.vel[1] = 0
					self.platform_speed_x = block.vel[0]	# save platform speed
					self.state = "standing"


		# Collision checking for enemies
		block_hit_list = pygame.sprite.spritecollide(self, bg.enemies, False)
		for enemy in block_hit_list:
			if self.rect.colliderect(enemy.rect):

				if dy > 0 and self.rect.bottom < enemy.rect.bottom:
					self.rect.bottom = enemy.rect.top
					self.vel[1] = 0
					self.state = "standing"
					self.platform_speed_x = enemy.vel[0]	# save platform speed
				
				# Check for damage and record time
				else:
					self.damage_time = self.damage(enemy, ticks)

		# Collision checking for objects
		block_hit_list = pygame.sprite.spritecollide(self, bg.objects, False)
		for thing in block_hit_list:
			if self.rect.colliderect(thing.rect):
				# Lose health when colliding with damaging objects
				if thing.deadly:
					self.damage_time = self.damage(thing, ticks)
				# Gain health when colliding with healthy objects
				elif thing.health:
					self.health += thing.health
					thing.kill()	# destroy object
			

	def damage(self, block, ticks):
		""" decreases health when running into things
			the player flashes red
		"""
		# Runs into spike platform
		if block.species == "spike" and self.damaged == False:
			self.flash()
			self.health -= 1
			self.damaged = True
			return ticks
		# Runs into enemy
		elif block.deadly == True and self.damaged == False:
			self.flash()
			self.health -= 1
			self.damaged = True
			return ticks
		else:
			if ticks - self.damage_time > 300:
				self.damaged = False
			return self.damage_time


	def update_image(self, ticks):
		""" updates player's displayed image
			cycles through walking images
		"""
		n = ticks % 800

		# Walking to the left
		if self.vel[0] < 0:
			if self.state == "jumping":
				self.default_image = R.IMAGES["walkL2.png"]
			elif self.walking == False:
				self.default_image = R.IMAGES["walkL1.png"]
			elif n <= 200:
				self.default_image = R.IMAGES["walkL1.png"]
			elif n <= 400 and n > 200:
				self.default_image = R.IMAGES["walkL2.png"]
			elif n <= 600 and n > 400:
				self.default_image = R.IMAGES["walkL3.png"]
			else:
				self.default_image = R.IMAGES["walkL2.png"]

		# Walking to the right
		elif self.vel[0] >= 0:
			if self.state == "jumping":
				self.default_image = R.IMAGES["walkR2.png"]
			elif self.walking == False:
				self.default_image = R.IMAGES["walkR1.png"]
			elif n <= 200:
				self.default_image = R.IMAGES["walkR1.png"]
			elif n <= 400 and n > 200:
				self.default_image = R.IMAGES["walkR2.png"]
			elif n <= 600 and n > 400:
				self.default_image = R.IMAGES["walkR3.png"]
			else:
				self.default_image = R.IMAGES["walkR2.png"]

	
	def flash(self):
		flash_image = self.default_image.copy()

		# Recolor all non-transparent pixels to red
		for x in range(flash_image.get_size()[0]):
			for y in range(flash_image.get_size()[1]):
				if flash_image.get_at([x, y]) != (255,255,255):
					flash_image.set_at([x, y], (178,34,34))
		self.default_image = flash_image
