import pygame
from Player import Player
from Background import Background
import resources as R

def main():
    pygame.init()

    #dimensions of screen
    screen = pygame.display.set_mode((R.SCREEN_WIDTH, R.SCREEN_HEIGHT))
    pygame.display.set_caption("Super Mudd World")

    #creating entities
    player = Player()
    background = Background()

    #states: in_game, gameover
    state = "in_game"

    done = False

    #time stuff
    clock = pygame.time.Clock()
    fps = 30 #time step        
    
    while not done:
        if state == "in_game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            
            screen.fill((0,0,0))    #erases past junk

            background.blit(screen) #blit things to screen
            player.blit(screen)

            state = player.update(1.0/fps, background)   #player update

        elif state == "gameover":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            background.endscreen(screen)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_q]:
                done = True
            elif pressed[pygame.K_SPACE]:
                state = "in_game"
                player = Player()
                background = Background()

        clock.tick(fps)
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
   main()
