import pygame

class Background(pygame.sprite.Sprite):

	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 395
	BOTTOM_MARGIN = 20

	def __init__(self):
		#load image
		self.image = pygame.image.load('background-1500.png').convert()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = self.image.get_rect()
		self.world_shift = 0
		self.title = "SUPER MUDD"
		self.platforms = []
		self.plat_positions = [
			[100, 300],
			[300, 200],
			[600, 240],
			[200, 360]
		]
		self.make_Platforms()
		
		#position
		self.rect.x = 0
		self.rect.y = 0

		self.vel = [0,0]

		#text 
		self.font = pygame.font.Font("Fipps-Regular.otf", 30)
		self.text = self.font.render(self.title, True, (0,0,0))

	def blit(self, screen):

		screen.blit(self.image, [self.rect.x, self.rect.y])
		screen.blit(self.text, (0,0))
		for i in self.platforms:
			i.blit(screen)

	def collision_check(self, player):
		collided = ""
		kill = False

		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(player, self.platforms, False)
		for block in block_hit_list:
			if player.vel[0] > 0:
				player.rect.right = block.rect.left
				collided += "right"
			elif player.vel[0] < 0:
				player.rect.left = block.rect.right
				collided += "left"

		collided = ""
		block_hit_list = pygame.sprite.spritecollide(player, self.platforms, False)
		for block in block_hit_list:
			# Reset our position based on the top/bottom of the object.
			if player.vel[1] > 0:
				player.rect.bottom = block.rect.top - 10
				collided += "bottom"
			elif player.vel[1] < 0:
				player.rect.top = block.rect.bottom + 10
				collided += "top"
			player.vel[1] = 0
		return collided, kill


	def make_Platforms(self):
		for i in self.plat_positions:
			new_plat = Platform(i[0],i[1])
			self.platforms += [new_plat]

	def shift_world(self, shift_x):
		"""when the user moves and we need to shift everything"""
		#the shift amount
		self.vel[0] += shift_x

		#shift all other things
		for platform in self.platforms:
			platform.vel[0] += shift_x

	def update(self, dt, collides):
		self.rect.x += self.vel[0] * dt
		self.rect.y += self.vel[1] * dt

		for platform in self.platforms:
			platform.rect.x += self.vel[0] * dt
			platform.rect.y += self.vel[1] * dt

class Platform:
	def __init__(self, x, y):
		self.image = pygame.image.load('redplat.png').convert()
		self.height = self.image.get_height()
		self.width = self.image.get_width()

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.vel = [0,0]

		self.type = "platform"

	def blit(self, screen):
		screen.blit(self.image, [self.rect.x,self.rect.y])
