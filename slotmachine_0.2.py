# Source File Name: slotmachine_0.2.py
# Author's Name: Hemangini Chauhan
# Last Modified By: Hemangini Chauhan
# Date Last Modified: Thursday June14, 2013
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the pygame module

  Version: 0.2 - * Spin or play are reset buttons are added. Clear the three wheels images with blank. 
                   Create label for entering bet amount.
"""

# import statements

import pygame, sys
from pygame.locals import *

pygame.init() 

#Display configuration
width, height = 520, 500
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('Slot Machine')

# set image for slot machine
background = pygame.image.load('slot machine.png')
screen.blit(background, (0,0))


# display a spin/play button
spin = pygame.image.load('play-spin.jpg')
screen.blit(spin, (350,420))

# display a reset button
reset = pygame.image.load('reset.jpg')
screen.blit(reset, (110,420))

# display a wheels 
blank = pygame.image.load('Blank.jpg')
screen.blit(blank, (101,207))
screen.blit(blank, (215,207))
screen.blit(blank, (328,207))
    
myfont = pygame.font.SysFont("Cambria", 20)
label = myfont.render("Place your bet:", 1, (255, 0, 0))
screen.blit(label, (140, 380))
pygame.display.flip()
def main():
    
    # set the main loop
    while True:
        pygame.display.update()

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
                
if __name__ == "__main__": main()