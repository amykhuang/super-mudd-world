import pygame, os

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 395
BOTTOM_MARGIN = 20
STEP = 3
GRAVITY = 1000

pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

IMAGES = {}
for i in os.listdir(os.path.join("data","images")):
	if i[-4:] == ".png":
		IMAGES[i] = pygame.image.load(os.path.join("data","images",i)).convert()
		IMAGES[i].set_colorkey((255,255,255))

SOUNDS = {}
for i in os.listdir(os.path.join("data","sounds")):
	if i[-4:] == ".wav":
		SOUNDS[i] = pygame.mixer.Sound(os.path.join("data","sounds",i))
		SOUNDS[i].set_volume(0.5)

FONTS = {}
for i in os.listdir(os.path.join("data","fonts")):
	if i[-4:] == ".otf":
		FONTS[i] = pygame.font.Font(os.path.join("data","fonts",i), 30)
