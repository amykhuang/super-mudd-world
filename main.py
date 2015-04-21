import pygame
import os

pygame.init()
#dimensions of screen
screen = pygame.display.set_mode((1000, 395))

#Loads player image and gets rid of background color (white)
player_imageR = pygame.image.load('spear1.png').convert()
player_imageL = pygame.image.load('spear1L.png').convert()
player_imageR.set_colorkey((255,255,255))
player_imageL.set_colorkey((255,255,255))

#loads background image
background_image = pygame.image.load('background.png').convert()

done = False

#Color and position (changeable) of box
is_blue = True
x = 0
y = 275

#times stuff
clock = pygame.time.Clock()

#Player default direction
default_player = player_imageR

#walk timer

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Changes color of block 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    #erases past junk
    screen.fill((0,0,0))

    #Copy background to screen and puts in default player
    screen.blit(background_image, [0,0])
    screen.blit(default_player, [x,y])
    
    #Tests for key presses and loads images
    pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_UP]: y  -= 3
    #if pressed[pygame.K_DOWN]: y  += 3
    
    if pressed[pygame.K_LEFT] and 0<x:
        default_player = player_imageL
        x  -= 3
        
    if pressed[pygame.K_RIGHT] and x<900:
        default_player = player_imageR
        x  += 3

    #Draws new rectangle
    if is_blue:
        color = (0,128, 255)
    else: color = (155, 200, 0)
    #pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))


    #Waits 1/60 second
    clock.tick(60)
    
    pygame.display.flip()



def walkcycle():
    """Makes the walk animation
    """

def walktimer():
    
