import pygame
import resources as R

class Friend(pygame.sprite.Sprite):

	def __init__(self, x, y, typ):
		pygame.sprite.Sprite.__init__(self)

		friend_dict = {	# [image]
			'ron': [
				R.IMAGES["ronbig.png"],
				[["Hello, my name", "is Ron"], ["What's your name?"]]
			]
		}

		self.image = friend_dict[typ][0]
		self.selfrect = self.image.get_rect()
		self.rect = pygame.Rect((x - 100, y + 64 - self.image.get_height()), \
			(self.image.get_width() + 100, self.image.get_height()))

		self.deadly = False
		self.species = typ
		self.speak = True

		self.text = friend_dict[typ][1]
	
	def show_text(self):
		textbox = TextBox()
		textbox.setText(self.text[0])
		return textbox

# character speech bubbles
class TextBox(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = R.FONTS['emulogic']
		self.image = pygame.Surface((250,120))
		self.image.fill(R.WHITE)
		self.x_pos = 30
		self.y_pos = 40
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)

	def setText(self, text):
		x_pos = self.x_pos
		y_pos = self.y_pos

		for line in text:
			x = self.font.render(line, False, (0, 0, 0))
			self.image.blit(x, (x_pos, y_pos))

			y_pos += 20


