# Source File Name: slotmachine_0.1.py
# Author's Name: Hemangini Chauhan
# Last Modified By: Hemangini Chauhan
# Date Last Modified: Thursday June 7, 2013
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the pygame module

  Version: 0.1 - * This version shows the window only.
"""

# import statements
import pygame,sys

pygame.init()
    
def main():
    width, height = 800, 600
    screen=pygame.display.set_mode((width, height))
    pygame.display.set_caption('Slot Machine')
    
    
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
if __name__ == "__main__": main()