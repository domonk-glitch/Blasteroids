# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from logger import log_state

def main():
    pygame.init
#    print('Starting Asteroids!')
#    print('Screen width: 1280')
#    print('Screen height: 720') 
#    log_state()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#    clock = pygame.time.Clock()
#    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
#
        screen.fill("black")
        pygame.display.flip()

#       dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
