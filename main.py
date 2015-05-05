import pygame
from Player import Player
from Background import Background

def main():
    """ Main game loop lives here.
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

        collides, kill = background.collision_check(player)

        #erases past junk
    	screen.fill((0,0,0))

        #blit things to screen
        background.blit(screen)
        player.blit(screen)

        #Tests for key presses and loads images
        pressed = pygame.key.get_pressed()

        #player update
        player.getEvent(pressed, background, collides)
        player.update(dt, background, collides)
        background.update(dt, collides)

        clock.tick(1/dt) #waits 1/24 second
        pygame.display.flip()

    pygame.quit()

def walkcycle():
    """Makes the walk animation
    """

def walktimer():
    """
    """


if __name__ == "__main__":
   main()
