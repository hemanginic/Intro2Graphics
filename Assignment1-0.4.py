'Author Name: Hemangini Chauhan'
'Date-modified: May 23 2013'
'Program: Your pet dragon is kidnapped by the dangerous dragon and you are trying to rescue your dragon.'
'         In order to win, you have to reach to the level 3 cave to rescue your pet from dangerous dragons'
'Version: 0.3: Created level 3 options and complete the code for the game'


import time

#Displays introduction of the game 	
def displayIntro():
	print ('Your pet dragon is kidnapped by dangerous dragons from Dragon Land.')
	print ('You came to Dragon Land to rescue your pet dragon from Dangerous dragons.')
	time.sleep(2)
	print ('There are caves on the Dragon Land.')
	print ('On the Dragon Land you will be facing lots of dragon.')
	time.sleep(1)
	print ('Some of them are friendly and let you go in.')
	print ('Others are dangerous dragon who will stop you to go ahead.')
	time.sleep(2)
	print ('You have to fight with them to enter the caves.')
	time.sleep(2)
	print ('In front of you there is two caves.')
	print
	
#Allows the player to make a decision and select a cave
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will you go into? (1 or 2)')
		cave = raw_input()
	return cave

#level 1 options
def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(2)
	print ('You went deeper inside...')
	print
	time.sleep(2)
		
	if chosenCave == "1":
		print ('The road is full of rocks and dangerous snakes.')
		dangerousCave()
				
	elif chosenCave == "2":
		print ('There are friendly dragons are playing in this cave.')
		friendlyCave()
	return chosenCave   

def friendlyCave():
	print('They welcome you...')
	print('Gives you the treasure and they show you another two path to go ahead....')
	print('But they dont know which road takes you to your pet dragon')
	
	chooseRoad=''
	while chooseRoad != '1' and chooseRoad != '2':
		print ('Which Road you want to follow? (1 or 2)')
		chooseRoad = raw_input()
		
		if chooseRoad == "1":
			yourWay2()
		elif chooseRoad == "2":
			yourWay2()
	
	
def dangerousCave():
	print ('You can escape from here...')	
	print ('There are two ways available.')
	
	#level 2 options
	chooseWay=''
	while chooseWay != '1' and chooseWay != '2':
		print ('Which way will you go into? (1 or 2)')
		chooseWay = raw_input()
		
		if chooseWay == "1":
			print ('You are attcked by the snacks and they try to harm you.')
			print ('You fight with them and move ahead')
			yourWay1()
			
		elif chooseWay == "2":
			print ('The drageons welcome you and gives you their treasure ')
			print ('You have two options to choose your way ahead from here.')
			yourWay1()
			return chooseWay

def yourWay1():
	print ('You can see there are another two ways to go in.')
	#level 3 options
	selectWay=''
	while selectWay != '1' and selectWay != '2':
		print ('Which way will you go into? (1 or 2)')
		selectWay = raw_input()
		
	if selectWay == "1":
			print ('The deadly fire spread all over you...')
			time.sleep(2)
			print ('It burn you badly....')
			time.sleep(2)
			print('You are dead.')
			
	elif selectWay == "2":
			print ('There is a big storm in here...')
			time.sleep(2)
			print ('The trees and animals hits you badly...')
			time.sleep(2)
			print ('you are not able to walk forward.')
			time.sleep(2)
			print ('You fainted. You loose!!!')
			return selectWay
	
def yourWay2():
	print('There are lots of crabs and spiders on the floor....')
	time.sleep(2)
	print('They crawl over your body...')
	print ('You ran and saw another two options avilable to go ahead.')
	#level 3 options
	selectOption=''
	while selectOption != '1' and selectOption != '2':
		print ('Which option want to select? (1 or 2)')
		selectOption = raw_input()
		
	if selectOption == "1":
		    print('Suddenly.....')
		    time.sleep(2)
		    print('The dragons and snacks attack you... ')
		    time.sleep(2)
		    print ('You fight with them...')
		    time.sleep(2)
		    print ('They hit you badly...')
		    time.sleep(2)
		    print('You are dead.')
	#winning option		
	elif selectOption == "2":
		    print('Suddenly.....')
		    time.sleep(2)
		    print('The Dangerous dragons attack you... ')
		    time.sleep(2)
		    print ('You fight with the dangerous dragon...')
		    time.sleep(2)
		    print ('They hit you badly...')
		    time.sleep(2)
		    print ('But you burn them to death...')
		    time.sleep(2)
		    print ('You win....You got your pet dragon back.')
	return selectOption
	

def main():
	
	#Ask player a question if he wants to play the game
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		checkCave(caveNumber)
	
	#Takes user inputs if they wants to play the game again
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
