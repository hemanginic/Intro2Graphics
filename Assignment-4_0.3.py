"""
File Name: Assignment-4_0.2.py
Author's Name: Hemangini Chauhan
Last modified by: Hemangini Chauhan
Date Last Modified: July 10, 2013
Program Description: Drive a Car without while avoiding crash with rocks. Fill the fuel to keep going. 
                     You will get fuel tank while driving, fill the fuel to keep going.
                     
                     
varsion-0.2 : step 3 of Cargame, add rock, fuel tank and background, move it,
              don't worry about collisions yet
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((850, 450))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mycar.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (500, mousey)
        
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("myrock.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.right += self.dx;
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 1
        self.rect.centery = random.randrange(0, 450)
    
           
class Road(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("track.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right += self.dx
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()
        
class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("carfuel.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right += self.dx
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()
def main():
    screen = pygame.display.set_mode((650, 450))
    pygame.display.set_caption("My Car Game")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    
    car = Car()
    rock1 = Rock()
    rock2 = Rock()
    rock3 = Rock()
    road = Road()
    fuel = Fuel()
    
    friendSprites = pygame.sprite.OrderedUpdates(road, car, fuel)
    rockSprites = pygame.sprite.Group(rock1, rock2, rock3)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #allSprites.clear(screen, background)
        #allSprites.update()
        #allSprites.draw(screen)
        
        
        friendSprites.update()
        rockSprites.update()
        friendSprites.draw(screen)
        rockSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
