"""
File Name: Assignment-4_0.2.py
Author's Name: Hemangini Chauhan
Last modified by: Hemangini Chauhan
Date Last Modified: July 10, 2013
Program Description: Drive a Car without while avoiding crash with rocks. Fill the fuel to keep going. 
                     You will get fuel tank while driving, fill the fuel to keep going.
                     
                     
varsion-0.4 : step 3 of Cargame, add multiple rocks, background sound and collisions,
              
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((890, 450))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("Problem with sound")
        else:
            pygame.mixer.init()
            self.sndKhach = pygame.mixer.Sound("khach.ogg")
            self.sndCrash = pygame.mixer.Sound("crash.ogg")
            self.sndCarEngine = pygame.mixer.Sound("carengine.ogg")
            self.sndCarEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (500, mousey)
        
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rock.png")
#
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.right += self.dx;
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, 450)
    
           
class Road(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("track1.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right += self.dx
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.right = screen.get_width()
        
        
class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load("rock.gif")
        self.image = pygame.image.load("fuel.png")
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.left += self.dx;
        if self.rect.left > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, 450)
    
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
    rock = Rock()
    road = Road()
    fuel = Fuel()
    
    friendSprites = pygame.sprite.OrderedUpdates(road, car, rock, fuel)
    rockSprites = pygame.sprite.Group(rock1, rock2, rock3)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
                
                #check collisions
        if car.rect.colliderect(fuel.rect):
            car.sndKhach.play()
            fuel.reset()
        if car.rect.colliderect(rock.rect):
            car.sndCrash.play()
            rock.reset()
            
        # for multiple rocks   
        hitRocks = pygame.sprite.spritecollide(car, rockSprites, False)

        if hitRocks:
            car.sndCrash.play()
            for theRock in hitRocks:
                theRock.reset()
        
            
                
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
            
