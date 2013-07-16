"""
File Name: Assignment-4_0.7.py
Author's Name: Hemangini Chauhan
Last modified by: Hemangini Chauhan
Date Last Modified: July 14, 2013
Program Description: Drive a Car without while avoiding crash with rocks. Fill the fuel to keep going. 
                     You will get fuel tank while driving, fill the fuel to keep going.
                     
                     
varsion-0.7: step 7 of Cargame, Change instruction, font, font size.
              
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((750, 450))

# display a car that is controlled by user
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        # sound controls
        if not pygame.mixer:
            print("Problem with sound")
        else:
            pygame.mixer.init()
            #play sound hen user catch the fuel tank
            self.sndKhach = pygame.mixer.Sound("khach.ogg") 
            #play sound hen user hits the rocks
            self.sndCrash = pygame.mixer.Sound("crash.ogg")
            #background sound
            self.sndCarEngine = pygame.mixer.Sound("carengine.ogg")
            self.sndCarEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (600, mousey)
        
# display rocks and update it, user should avoid it.        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rock.png")

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
    
# background of the screen which keeps moving         
class Road(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("road.jpg")
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
        
# disply fuel tanks, user have to catch it to get life        
class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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
        
 # display scores on screen and update it        
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "lives: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (0, 0, 255))
        self.rect = self.image.get_rect()
        
# play game 
def game():       
    
    pygame.display.set_caption("Drive a Car")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    car = Car()
    rock1 = Rock()
    rock2 = Rock()
    rock3 = Rock()
    rock4 = Rock()
    road = Road()
    fuel = Fuel()
    scoreboard = Scoreboard()
    
    friendSprites = pygame.sprite.OrderedUpdates(road, car, fuel)
    rockSprites = pygame.sprite.Group(rock1, rock2, rock3, rock4)
    scoreSprite = pygame.sprite.Group(scoreboard)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
                
        #check collisions
        # add lives if car hits the fuel tank
        if car.rect.colliderect(fuel.rect):
            car.sndKhach.play()
            fuel.reset()
            scoreboard.score += 10
        
            
        # for multiple rock hit
        hitRocks = pygame.sprite.spritecollide(car, rockSprites, False)

        if hitRocks:
            car.sndCrash.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False    
            for theRock in hitRocks:
                theRock.reset()
        
        #updates all sprites
        friendSprites.update()
        rockSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        rockSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
       
    # stop the engine 
    car.sndCarEngine.stop() 
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
# display instruction at the beginning of the game with score   
def instructions(score):
    car = Car()
    road = Road()
    
    allSprites = pygame.sprite.OrderedUpdates(road, car)
    insFont = pygame.font.SysFont('arnprior', 20)
  
    instructions = (
    "",
    "",
    "Drive a Car.     Last score: %d" % score ,
     "",
    "Instructions:  ",
    "You are driving a car.",
    "Keep driving to get the fuel tank",
    "but be careful not to crash with rocks",    
    "Your car will crash if you hit many times.",
    "Steer with mouse",
    "",
    "Click to start the game.",
    "Escape to quit..."
    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, ( 0, 0, 255))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    car.sndCarEngine.stop()
    pygame.mouse.set_visible(True)
    return donePlaying
        
    
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
            
if __name__ == "__main__":
    main()
            
