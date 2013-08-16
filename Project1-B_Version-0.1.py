"""
Program Name: Lunch Time
Author: Shauna Willmore  and Hemangini Chauhan
Last Modfied By: Shauna Willmore and Hemangini Chauhan
Date last Modified: 05/08/2013


Program description: User plays a fish swimming around a pool of water. The goal is to eat
as many little fish/worms as possible(points are rewarded for each "consumed"), and to avoid all 
blow fish/poisin flakes(will result in a life lost if came into contact too many times). Little fish award 100 points
and worms award 50 points.

Revision History: 
Project1-A Version 0.1 - Adding ocean sprites, blowfish sprite, food sprite and user fish sprite.
Game start and game end screen are added.
Project1-A Version 0.2 - the enemy sprite (shark) changed to blow fish. Try to add 3 different levels to the game. 
Only one level is working for now (Press 1 for easy game).
Project1-A Version 0.3 - All three levels are added. But adding points for eating worm and sounds when user fish 
hits (eats) the worm is not added.
Project1-A Version 0.4 - All three levels are added. Collision for worm and poisonous food flakes are added.
Project1-A Version 0.5 - Worm and poison flakes added. Sounds working for all colisions. Scores awarded to the
user edited to be different for worms (was 100, now 50).

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
        
        #Sounds 
        else:
            pygame.mixer.init()
            #User hits fish
            self.sndHitFish = pygame.mixer.Sound("hitFish.wav")
            #User hits blowfish
            self.sndBlowfish = pygame.mixer.Sound("hitBlowfish.wav")
            #User hits poisin flake
            self.sndEatPoisin = pygame.mixer.Sound("eatpoison.wav")
            #User hits a worm
            self.sndEatWorm = pygame.mixer.Sound("eatworm.wav")
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
        
class Worm(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("worm.gif")
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


#The blowfish or enemy the user needs to avoid      
class Blowfish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blowfish.gif")
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
        
        
#The moustach or enemy the user needs to avoid      
class Moustache(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("evilfish1.gif")
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
        
#The poison ivy or enemy the user needs to avoid           
class PoisonIvy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("poisonivy.gif")
        #self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        
    
    def update(self):
        
        self.rect.centerx += self.dx

        if self.rect.right < -1:
            self.reset()
            
        #self.rect.right += self.dx;
        #if self.rect.right > screen.get_width():
           # self.reset()
            
    def reset(self):
        self.rect.right = 0
        self.rect.centery = random.randrange(0, 600)
        self.dy = random.randrange(4, 8)
        self.dx = random.randrange(20, 22)



#Poisin flake user needs to avoid     
class Flake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flake.gif")
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

#Easiest Level -- Contains 1 Enemy and 1 Friend
def levelone():
    pygame.display.set_caption("Lunch Time!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    userfish = Userfish()
    fishfood = Fishfood()
    blowfish1 = Blowfish()
    water = Water()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(water, fishfood, userfish)
    blowfishSprites = pygame.sprite.Group(blowfish1)
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
            scoreboard.score += 100

        #Check to see if the user has come in contact with a blowfish. If they have subtract
        #a life.    
        hitBlowfishs = pygame.sprite.spritecollide(userfish, blowfishSprites, False)
        if hitBlowfishs:
            userfish.sndBlowfish.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theBlowfish in hitBlowfishs:
                theBlowfish.reset()
        
        friendSprites.update()
        blowfishSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        blowfishSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    userfish.sndWater.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#Medium Level -- Contains 3 enemies and 2 Friends
def leveltwo():
    pygame.display.set_caption("Lunch Time!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    userfish = Userfish()
    worm = Worm()
    fishfood = Fishfood()
    flake1 = Flake()
    flake2 = Flake()
    flake3 = Flake()
    water = Water()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(water, fishfood, worm, userfish)
    flakeSprites = pygame.sprite.Group(flake1, flake2, flake3)
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
            scoreboard.score += 100
            
        #Check to see if the user has come into contact with a worm. If they have
        #add points to the score
        if userfish.rect.colliderect(worm.rect):
            userfish.sndEatWorm.play()
            worm.reset()
            scoreboard.score += 50
            
        #Check to see if the user has come in contact with a poisin flake. If they have subtract
        #a life.    
        hitflakes = pygame.sprite.spritecollide(userfish, flakeSprites, False)
        if hitflakes:
            userfish.sndEatPoisin.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theflake in hitflakes:
                theflake.reset()
        
        friendSprites.update()
        flakeSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        flakeSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    userfish.sndWater.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#Hard Level -- Contains 5 enemies and 2 friends
def levelthree():
    pygame.display.set_caption("Lunch Time!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    userfish = Userfish()
    fishfood = Fishfood()
    blowfish1 = Blowfish()
    blowfish2 = Blowfish()
    flake1 = Flake()
    flake2 = Flake()
    flake3 = Flake()
    worm = Worm()
    water = Water()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(water, fishfood, worm, userfish)
    blowfishSprites = pygame.sprite.Group(blowfish1, blowfish2)
    flakeSprites = pygame.sprite.Group(flake1, flake2, flake3)
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
            scoreboard.score += 100
        
        #Check to see if the user has come into contact with a worm. If they have
        #add points to the score
        if userfish.rect.colliderect(worm.rect):
            userfish.sndEatWorm.play()
            worm.reset()
            scoreboard.score += 50
            
        #Check to see if the user has come in contact with a blowfish. If they have subtract
        #a life.    
        hitblowfishs = pygame.sprite.spritecollide(userfish, blowfishSprites, False)
        if hitblowfishs:
            userfish.sndBlowfish.play()
            scoreboard.lives -= 5
            if scoreboard.lives <= 0:
                keepGoing = False
            for theblowfish in hitblowfishs:
                theblowfish.reset()
        
        #Check to see if the user has come in contact with a poisin flake. If they have subtract
        #a life.    
        hitflakes = pygame.sprite.spritecollide(userfish, flakeSprites, False)
        if hitflakes:
            userfish.sndEatPoisin.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theflake in hitflakes:
                theflake.reset()
        
        
        friendSprites.update()
        blowfishSprites.update()
        flakeSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        blowfishSprites.draw(screen)
        flakeSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    userfish.sndWater.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

def levelfour():
    pygame.display.set_caption("Lunch Time!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    userfish = Userfish()
    fishfood = Fishfood()
    blowfish1 = Blowfish()
    blowfish2 = Blowfish()
    moustache1 = Moustache()
    moustache2 = Moustache()
    poisonIvy1 = PoisonIvy()
    poisonIvy2 = PoisonIvy()
    poisonIvy3 = PoisonIvy()
    worm = Worm()
    water = Water()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(water, fishfood, worm, userfish)
    blowfishSprites = pygame.sprite.Group(blowfish1, blowfish2)
    moustacheSprites = pygame.sprite.Group(moustache1, moustache2)
    poisonIvySprites = pygame.sprite.Group(poisonIvy1, poisonIvy2, poisonIvy3)
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
            scoreboard.score += 100
        
        #Check to see if the user has come into contact with a worm. If they have
        #add points to the score
        if userfish.rect.colliderect(worm.rect):
            userfish.sndEatWorm.play()
            worm.reset()
            scoreboard.score += 50
            
        #Check to see if the user has come in contact with a blowfish. It kills the User fish 
        hitblowfishs = pygame.sprite.spritecollide(userfish, blowfishSprites, False)
        if hitblowfishs:
            userfish.sndBlowfish.play()
            scoreboard.lives -= 5
            if scoreboard.lives <= 0:
                keepGoing = False
            for theblowfish in hitblowfishs:
                theblowfish.reset()
        
        #Check to see if the user has come in contact with a evilfish. It kills the User fish
        hitevilfish = pygame.sprite.spritecollide(userfish, moustacheSprites, False)
        if hitevilfish:
            userfish.sndEatPoisin.play()
            scoreboard.lives -= 5
            if scoreboard.lives <= 0:
                keepGoing = False
            for theevilfish in hitevilfish:
                theevilfish.reset()
        
        #Check to see if the user has come in contact with a poisin ivy. It subtract a life.    
        hitPoisonIvy = pygame.sprite.spritecollide(userfish, poisonIvySprites, False)
        if hitPoisonIvy:
            userfish.sndEatPoisin.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for thepoisonIvy in hitPoisonIvy:
                thepoisonIvy.reset()
        
        
        friendSprites.update()
        blowfishSprites.update()
        moustacheSprites.update()
        poisonIvySprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        blowfishSprites.draw(screen)
        moustacheSprites.draw(screen)
        poisonIvySprites.draw(screen)
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
    "to Mr.Blowfish! He will eat your little guy!",
    "Don't eat the poisonous food flakes!",
    "Remember...",
    "Just keep swimming!",
    "",
    "Control Fishy with the mouse!",
    "",
    "Press 1 for Easy",
    "",
    "Press 2 for Medium",
    "",
    "Press 3 for Hard (Touching Mr.Blowfish results in instant DEATH)",
    "",
    "Press 4 for Hard (Touching Moustach fish results in instant DEATH)"
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
               donePlaying = False
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = False
                 if event.key == pygame.K_1:
                    levelone()
                    keepGoing = False
                    donePlaying = True
                 if event.key == pygame.K_2:
                    leveltwo()
                    keepGoing = False
                    donePlaying = True
                 if event.key == pygame.K_3:
                    levelthree()
                    keepGoing = False
                    donePlaying = True 
                 if event.key == pygame.K_4:
                    levelfour()
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

   
 #game over screen  
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
    "Game Over... ",
    "     ",
    "Do you want to play again?",
    "     ",
    "Click to return to the main menu!",
    "     ",
    "Press escape to quit!"
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
    #if user want to play game
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions()
        donePlaying = end(score)


if __name__ == "__main__":
    main()
    
    
