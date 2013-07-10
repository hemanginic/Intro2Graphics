"""
File Name: Assignment-4_0.2.py
Author's Name: Hemangini Chauhan
Last modified by: Hemangini Chauhan
Date Last Modified: July 9, 2013
Program Description: Drive a Car without while avoiding crash with rocks. Fill the fuel to keep going. 
                     You will get fuel tank while driving, fill the fuel to keep going.
                     
                     
varsion-0.2 : step 2 of Cargame, add rock, move it,
              don't worry about collisions yet
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((850, 450))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car1.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (150, mousey)
        
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rock4.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        'speed of the rock'
        self.dx = 5
    
    
    def update(self):
        self.rect.centery += self.dx
        'if the rock go out of screen'
        if self.rect.top > screen.get_height():
            self.reset()
            
    'reset the rock sprite'
    def reset(self):
        
        self.rect.top = 0
        self.rect.centerx = random.randrange(0,screen.get_width())
        
        
def main():
    screen = pygame.display.set_mode((850, 450))
    pygame.display.set_caption("My Car Game")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    car = Car()
    rock = Rock()
    
    allSprites = pygame.sprite.Group(car, rock)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
