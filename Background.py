import pygame

class Background:

	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 395
	BOTTOM_MARGIN = 20

	def __init__(self):
		#load image
		self.image = pygame.image.load('background-1500.png').convert()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.title = "SUPER MUDD"
		self.platforms = []
		self.plat_positions = [
			[100, 250],
			[300, 200],
			[600, 240],
			[200, 360]
		]
		self.make_Platforms()
		
		#position
		self.x = 0
		self.y = 0

		#text 
		self.font = pygame.font.Font("Fipps-Regular.otf", 30)
		self.text = self.font.render(self.title, True, (0,0,0))

	def blit(self, screen):

		screen.blit(self.image, [self.x, self.y])
		screen.blit(self.text, (0,0))
		for i in self.platforms:
			i.blit(screen)

	def collision_check(self, player):
		collided = ""
		kill = False

		for j in self.platforms:
			if j.type == "platform":
				i = j.rect
				#print player.get_rect().right, i.left
				player.get_rect().move_ip(0,1)
				if player.get_rect().colliderect(i):
					if player.get_rect().bottom >= i.top and player.get_rect().top <= i.top:
						collided += "bottom"
						player.get_rect().bottom = i.top+1
					player.get_rect().move_ip(0,-2)
				if player.get_rect().colliderect(i):
					if player.get_rect().top <= i.bottom and player.get_rect().bottom >= i.bottom:
						collided += "top"
						player.get_rect().top = i.bottom
				player.get_rect().move_ip(1,1)
				if player.get_rect().colliderect(i):
					if player.get_rect().right >= i.left and player.get_rect().left <= i.left:
						collided += "right"
						player.get_rect().right = i.left+1
				player.get_rect().move_ip(-2,0)
				if player.get_rect().colliderect(i):
					if player.get_rect().left <= i.right and player.get_rect().right >= i.right:
						collided += "left"
						player.get_rect().left = i.right-1
				player.get_rect().move_ip(1,0)
		return collided, kill


	def make_Platforms(self):
		for i in self.plat_positions:
			new_plat = Platform(i[0],i[1])
			self.platforms += [new_plat]
		

class Platform:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load('redplat.png').convert()
		self.height = self.image.get_height()
		self.width = self.image.get_width()
		self.rect = pygame.Rect([self.x, self.y],[self.width,self.height])
		self.type = "platform"

	def blit(self, screen):
		screen.blit(self.image, [self.x,self.y])
