import pygame
from player import Player
from maps import *
import resources as R

# TODO
# smaller rects for collisions
# fix moving enemy collision bug

# when it gets to end, player can move past center of screen

class Game:
    def __init__(self):
        self.level = 0

    def main(self):
        pygame.init()

        #dimensions of screen
        screen = pygame.display.set_mode((R.SCREEN_WIDTH, R.SCREEN_HEIGHT))
        pygame.display.set_caption("Super Mudd World")

        #creating entities
        player = Player()
        background = Map00()

        #states: in_game, gameover
        state = "in_game"

        done = False

        clock = pygame.time.Clock()
        fps = 20 #time step        
        
        while not done:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if state == "in_game":
                screen.fill(R.BLACK)    #erases past junk

                background.blit(screen, 1.0/fps) #blit things to screen
                player.blit(screen)

                state = player.update(1.0/fps, background)   #player update

            elif state == "gameover":
                endscreen = Endscreen(screen)

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
    g = Game()
    g.main()
