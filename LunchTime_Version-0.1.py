"""
Program Name: Lunch Time
Author: Shauna Willmore  and Hemangini Chauhan
Last Modfied By: Shauna Willmore and Hemangini Chauhan
Date last Modified: 08/03/2013


Program description: User plays a fish swimming around a pool of water. The goal is to eat
as many little fish as possible(points are rewarded for each "consumed", and to avoid all 
blow fish(will result in a life lost if came into contact). There are worms flotting in the 
water that user can consume and gain points.

Revision History: 
Project1-A Version 0.1 - Adding ocean sprites, shark sprite, food sprite and user fish sprite.
Game start and game end screen are added.
"""

import pygame, random

pygame.init()

#Screensize
screen = pygame.display.set_mode((950, 600))

#The fish the user controls
class Userfish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("userfish.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        #Sound isnt working
        if not pygame.mixer:
            print("Theres a problem with the sound")
        
        #Sounds for when the user consumes a fish, gets hit by a shark and the background sound
        else:
            pygame.mixer.init()
            #User hits fish
            self.sndHitFish = pygame.mixer.Sound("hitFish.wav")
            #User hits shark
            self.sndShark = pygame.mixer.Sound("hitShark.wav")
            #Background
            self.sndWater = pygame.mixer.Sound("water.wav")
            self.sndWater.play(-1)
        
    def update(self):
        #character (userfish) will move up and down
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (700, mousey)
        
#The fish the user will need to consume in order to gain points                
class Fishfood(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fishfood.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.left += self.dx
        if self.rect.left > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, 600)

#The shark or enemy the user needs to avoid      
class Shark(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sharkk.gif")
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.right += self.dx;
        if self.rect.right > screen.get_width():
            self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, 600)

#The scrolling background image (water)    
class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ocean.gif")
        self.images=self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.right += self.dy
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.right = screen.get_width()

#How the score is kept/updated
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont('helvetica',30)
        
    def update(self):
        self.text = "Lives: %d, Score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
 
def game():
    pygame.display.set_caption("Lunch Time!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    userfish = Userfish()
    fishfood = Fishfood()
    shark1 = Shark()
    shark2 = Shark()
    shark3 = Shark()
    water = Water()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(water, fishfood, userfish)
    sharkSprites = pygame.sprite.Group(shark1, shark2, shark3)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        
        #Check to see if the user has come into contact with a little fish. If they have
        #add points to the score
        if userfish.rect.colliderect(fishfood.rect):
            userfish.sndHitFish.play()
            fishfood.reset()
            scoreboard.score += 50
            
        #Check to see if the user has come in contact with a shark. If they have subtract
        #a life.    
        hitSharks = pygame.sprite.spritecollide(userfish, sharkSprites, False)
        if hitSharks:
            userfish.sndShark.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theShark in hitSharks:
                theShark.reset()
        
        friendSprites.update()
        sharkSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        sharkSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    userfish.sndWater.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#opening screen    
def instructions():
    pygame.display.set_caption("Lunch Time!")

    userfish = Userfish()
    water = Water()
    
    allSprites = pygame.sprite.Group(water, userfish)
    insFont = pygame.font.SysFont('helvetica',30)
    insLabels = []
    instructions = (
    "Its lunch time,",
    "and Fishy is hungry!",
    "",
    "Swim and eat ONLY fish!",
    "Be careful not to swim too close",    
    "to the sharks! The sharks will eat",
    "your little guy. We dont want that!",
    "Just keep swimming!",
    "",
    "Control Fishy with the mouse!",
    "",
    "Click = Start",
    "",
    "Escape = Quit"
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
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
        
    userfish.sndWater.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying
   
   
def end(score):
    pygame.display.set_caption("Lunch Time!")

    userfish = Userfish()
    water = Water()
    
    
    allSprites = pygame.sprite.Group(water, userfish)
    insFont = pygame.font.SysFont('helvetica',30)
    insLabels = []
    instructions = (
    "     ",
    "     ",
    "     ",
    "Lunch Time!.     Last score: %d" % score ,
    "     ",
    "     ",
    "Game is over... ",
    "     ",
    "Do you want to play again?",
    "     ",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    #handle if the user want to continue the game by clicking the mouse or just simply want to quit 
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
            screen.blit(insLabels[i], (80, 30*i))

        pygame.display.flip()
        
    userfish.sndWater.stop()     
    pygame.mouse.set_visible(True)
    return donePlaying
   
   
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions()
        #if not donePlaying:
        score = game()
        donePlaying = end(score)


if __name__ == "__main__":
    main()
    
    
