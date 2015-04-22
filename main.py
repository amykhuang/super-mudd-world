import pygame
from Sprite import *
from Background import *

def main():
    """ Main game loop lives here. Also loading pictures and stuff.
    """
    pygame.init()

    screen_width = 1000
    screen_height = 395
    screen = pygame.display.set_mode((screen_width, screen_height))  #dimensions of screen

    #creating stuff
    sprite = Sprite()
    background = Background()

    done = False

    #times stuff
    clock = pygame.time.Clock()

    #Player default direction
    default_player = sprite.imageR

    #Text 
    font = pygame.font.Font("Fipps-Regular.otf", 30)
    text = font.render("SUPER MUDD", True, (0,0,0))

    #Sound
    move_sound = pygame.mixer.Sound('smb_jumpsmall.wav')
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #erases past junk
    	screen.fill((0,0,0))
        
        #Copy background to screen and puts in default player
        screen.blit(background.image, [background.x,background.y])
        screen.blit(default_player, [sprite.x,sprite.y])

        #Text Stuff
        screen.blit(text,(0, 0))
        
        #Tests for key presses and loads images
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            pass

        #if pressed[pygame.K_DOWN]: y  += 3

        if pressed[pygame.K_LEFT] and sprite.x>0:
            default_player = sprite.imageL
            if sprite.x < 200 or bX > -200:
            	sprite.x -= 3
            elif background.x < 200: 
            	background.x += 3

        if pressed[pygame.K_RIGHT] and sprite.x<900:
            default_player = sprite.imageR
            if sprite.x < 200:
            	sprite.x += 3
            elif background.x > screen_width - background.width:
            	background.x -= 3
            #move_sound.play()

        
        clock.tick(24) #waits 1/24 second
        
        pygame.display.flip()



def walkcycle():
    """Makes the walk animation
    """

def walktimer():
    """
    """

def jump():
    """ Makes sprite jump when up key is pressed
    """


    

if __name__ == "__main__":   # did we just RUN this file?
   main()                   # if so, we call main()
