import pygame
import numpy as np
import sys

white = (255,255,255)
black = (0,0,0)


def init(res):
    #init pygame
    pygame.init()
    screen = pygame.display.set_mode(res)
    return(screen)

def draw(coords,res):
    screen = init(res)
    
    while(True):
        
        #check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear
        screen.fill(white)

        #draw
        pygame.draw.aalines(screen, black, False, coords, 2)

        #update the screen
        pygame.display.update()
