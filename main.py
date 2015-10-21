import pygame
from player import Player
from maps import *
import resources as R

# TODO
# smaller rects for collisions
# text boxes
# bug: can still jump after walking off a platform

class Game:
    def __init__(self):
        self.level = 0

    def play(self):
        pygame.init()

        # Dimensions of screen
        screen = pygame.display.set_mode((R.SCREEN_WIDTH, R.SCREEN_HEIGHT))
        pygame.display.set_caption("Super Mudd World")

        # Create the player and the environment
        player = Player()
        background = Map00()

        # States include: in_game, speaking, gameover
        state = "in_game"

        done = False

        clock = pygame.time.Clock()
        fps = 30    # frames per second      
        
        while not done:
            pressed = pygame.key.get_pressed()  # get keypress

            # Response to exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            ### Game modes

            if state == "in_game":
                screen.fill(R.BLACK)    # erases past junk

                background.blit(screen, 1.0/fps) # blit things to screen
                player.blit(screen)

                # Update the player and get its state
                state = player.update(1.0/fps, background, pressed)

            elif state == "speaking":
                print "Speaking"
                
            elif state == "gameover":
                endscreen = Endscreen(screen)

                if pressed[pygame.K_q]:
                    done = True
                elif pressed[pygame.K_SPACE]:
                    state = "in_game"
                    player = Player()
                    background = Map00()

            clock.tick(fps)
            pygame.display.flip()


        pygame.quit()

if __name__ == "__main__":
    g = Game()
    g.play()
