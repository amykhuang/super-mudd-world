import pygame
from Player import Player
from Background import Background

def main():
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
    fps = 30 #time step        
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill((0,0,0))    #erases past junk

        background.blit(screen) #blit things to screen
        player.blit(screen)

        player.update(1.0/fps, background)   #player update

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
   main()
