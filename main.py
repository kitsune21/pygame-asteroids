import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    game()

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing asteroids.")
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()