import pygame
import resources as R

class Friend(pygame.sprite.Sprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		friend_dict = {	# [image]
			'ron': [R.IMAGES["ronbig.png"], ["Hello, my name is Ron", "What's your name?"]]
		}

		self.image = friend_dict[typ][0]
		self.selfrect = self.image.get_rect()
		self.rect = pygame.Rect((x - 100, y + 64 - self.image.get_height()), (self.image.get_width() + 100, self.image.get_height()))
		print self.rect.contains(self.selfrect)

		self.deadly = False
		self.species = typ
		self.speak = True

		self.text = friend_dict[typ][1]
	
	def show_text(self, screen):
		textbox = TextBox(self.text[0])

		testsurface = pygame.Surface((200,80))
		testsurface.fill(R.WHITE)

		font = R.FONTS['emulogic']
		x = font.render('h', False, R.BLACK)
		testsurface.blit(x, (30, 40))

		screen.blit(testsurface, [30, 30])

	def update(self, screen):
		self.show_text(screen)


# character speech bubbles
class TextBox(pygame.sprite.Sprite):
	def __init__(self, text):
		pygame.sprite.Sprite.__init__(self)
		self.font = R.FONTS['emulogic']
		self.image = pygame.Surface((200,80))
		self.image.fill(R.WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
		self.setText(text)

	def setText(self, text):
		tmp = pygame.display.get_surface()
		x_pos = self.rect.left + 5
		y_pos = self.rect.top + 5

		for t in text:
			x = self.font.render(t, False, R.BLACK)
			self.image.blit(x, (x_pos, y_pos))
			x_pos += 10

			if (x_pos > self.image.get_width() - 5):
				x_pos = self.rect.left + 5
				y_pos += 10

