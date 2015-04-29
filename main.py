import pygame
from Player import Player
from Background import Background

def main():
    """ Main game loop lives here. Also loading pictures and stuff.
    """
    pygame.init()

    #dimensions of screen
    screen = pygame.display.set_mode((Background.SCREEN_WIDTH, Background.SCREEN_HEIGHT))
    pygame.display.set_caption("Super Mudd World")

    #creating entities
    player = Player()
    background = Background()

    done = False

    #time stuff
    clock = pygame.time.Clock()
    dt = 1.0/24 #time step        
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #erases past junk
    	screen.fill((0,0,0))
        
        #Copy background to screen and puts in default player
        screen.blit(background.image, [background.x, background.y])
        screen.blit(player.default_image, [player.x, player.y])

        #Text Stuff
        screen.blit(background.text,(0, 0))
        
        #Tests for key presses and loads images
        pressed = pygame.key.get_pressed()

        #player update
        player.keyPress(pressed, background)
        player.update(dt)

        clock.tick(1/dt) #waits 1/24 second
        pygame.display.flip()



def walkcycle():
    """Makes the walk animation
    """

def walktimer():
    """
    """


if __name__ == "__main__":
   main()
