import os, pygame
import pytmx

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640
BOTTOM_MARGIN = 20
STEP = 4
GRAVITY = 1000

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

IMAGES = {}
for i in os.listdir(os.path.join("data","images")):
	if i[-4:] == ".png":
		IMAGES[i] = pygame.image.load(os.path.join("data","images",i)).convert()
		IMAGES[i].set_colorkey((255,255,255))

TMX = {}
#for i in os.listdir(os.path.join("data","tmx")):
#	if i[-4:] == ".tmx":
#		TMX[i] = pytmx.TiledMap(i)
for i in os.listdir(os.path.join("data","tmx")):
	if i[-4:] == ".png":
		TMX[i] = pygame.image.load(os.path.join("data","tmx",i)).convert()

SOUNDS = {}
for i in os.listdir(os.path.join("data","sounds")):
	if i[-4:] == ".wav":
		SOUNDS[i] = pygame.mixer.Sound(os.path.join("data","sounds",i))
		SOUNDS[i].set_volume(0.5)

FONTS = {}
FONTS['Fipps Medium'] = pygame.font.Font(os.path.join("data","fonts","Fipps-Regular.otf"), 30)
FONTS['Fipps Small'] = pygame.font.Font(os.path.join("data","fonts","Fipps-Regular.otf"), 20)

MAPS = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]]
