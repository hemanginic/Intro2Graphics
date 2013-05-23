'Author Name: Hemangini Chauhan'
'Date-modified: May 23 2013'
'Program: Your pet dragon is kidnapped by the dangerous dragon and you are trying to rescue your dragon.'
'Version- 0.1 : Created a decision level for player to choose from.'
'               Once the player choose the option he will get another two option in order to procced'

import time

	
def displayIntro():
	
	print ('You are on a Dragon Land to rescue your pet dragon from the group of Dangerous dragons')
	print ('On the Dragon Land you will be facing lots of dragon')
	time.sleep(2)
	print ('Some of them are friendly and let you go in .')
	print ('Others are dangerous dragon who will stop you to go ahed.')
	time.sleep(2)
	print ('You have to fight with them to enter the cave')
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

	
def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('You went deeper inside...')
	print
	time.sleep(2)
		
	if chosenCave == "1":
		print ('The road is full of rocks and dangerous snakes.')
		dangerousCave()
				
	elif chosenCave == "2":
		print ('There are friendly dragons are playing in this cave ')
		friendlyCave()
	return chosenCave   

def friendlyCave():
	print('They welcomes you...')
	print('Gives you the tresure and they show you another two path to go ahead....')
	print('But they dont know which road takes you to your pet dragon')
	
	chooseRoad=''
	while chooseRoad != '1' and chooseRoad != '2':
		print ('Which Road you want to follow? (1 or 2)')
		chooseRoad = raw_input()
		
		
		if chooseRoad == "1":
			print ('There are dangerous dragons try to stop you')
			print ('You fight with them and run ahead.')
			print ('dbsljfvhnxkv')
		elif chooseRoad == "2":
			print ('There is a big jungle with Hyenas, Wolfs and Snacks ')
			print ('You have to escape your self to proceed ahead.')
			
	return chooseRoad
	
	
def dangerousCave():
	print ('You can escape from here...')	
	print ('There are two ways available.')
	
	chooseWay=''
	while chooseWay != '1' and chooseWay != '2':
		print ('Which way will you go into? (1 or 2)')
		chooseWay = raw_input()
		
		
		if chooseWay == "1":
			print ('You are attcked by the snacks and they try to harm you.')
			print ('You fight with them and move ahead')
			print ('You have two options to choose your way ahead from here.')
			
		elif chooseWay == "2":
			print ('The drageons welcomes you and gives you their tresure ')
			print ('You have two options to choose your way ahead from here.')
			return chooseWay


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
