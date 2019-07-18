import random
from time import sleep


def main():

	# Generating list which consists of 10 lists, each of which has 10 zroes in it.
	mapa = [[0] * 10 for i in range(10)]
	

	print()
	print("**** BATTLESHIPS ****")
	print()
	sleep(1)
	print("Currently, the sea is empty and calm.")
	print()
	sleep(1)

	printMap(mapa)
	sleep(1)

	deployUserShips(mapa)
	printMap(mapa)
	
	deployComputerShips(mapa)
	printMap(mapa)

	battle(mapa)
	


def printIndexes():
	"""Prints the column indexes with two white spaces at the begining and at the end."""
	
	print("  ", end="")
	for i in range(10):
		print(i, end="")
	print("  ")	


def printMap(mapa):
	"""Prints the map of the sea.
		
		VALUE LEGEND:

		0 - Empty field
        1 - Location of the user ship (print '@' on map)
        2 - Location of the computer ship (hidden from map)
        3 - Computer ship is sunk (print '!' on map)
        4 - User ship is sunk (print 'x' on map)
        5 - User missed (print '-' on map)
        6 - Computer missed (hidden from map)"""

	print()
	printIndexes()
	for row in range(10):
		print(f"{row}|", end="")		
		for column in range(10):
			if mapa[row][column] == 0 or mapa[row][column] == 2:
				print(" ", end="")
			elif mapa[row][column] == 1:
				print("@", end="")	
			elif mapa[row][column] == 3:
				print("x", end="")
			elif mapa[row][column] == 4:
				print("!", end="")
			elif mapa[row][column] == 5:
				print("-", end="")	
			else:
				print(" ", end="")			
		print(f"|{row}")
	printIndexes()
	print()


def deployUserShips(mapa):
	"""Prompts the user to enter the coordinates for his/her 5 ships."""

	for i in range(1, 6):
		
		# If the user enters something that cannot be cast into integer
		try:
			column = int(input(f"Enter the X coordinate for ship no. {i}: "))
		except:
			column = -1

		# The X coordinate cannot be out of bounds
		if column < 0 or column > 9:
			while column < 0 or column > 9:
				try:
					column = int(input("The X coordinate must be a number between 0 and 9: "))
				except:
					column = -1	
		
		# If the user enters something that cannot be cast into integer
		try:
			row = int(input(f"Enter the Y coordinate for ship no. {i}: "))
		except:
			row = -1

		# The Y coordinate cannot be out of bounds
		if row < 0 or row > 9:
			while row < 0 or row > 9:
				try:
					row = int(input("The Y coordinate must be a numbeer between 0 and 9: "))
				except:
					row = -1	

		# If the coordinates point to an empty field, deploy the ship - else, reprompt the user
		if mapa[row][column] == 0:
			mapa[row][column] = 1
		else:
			i -=1	


def deployComputerShips(mapa):
	"""The computer deploys 5 ships on random locations on the map."""
	
	print("THE COMPUTER DEPLOYS ITS SHIPS!")
	print()
	sleep(1)

	i = 1
	while i <= 5:
		column = random.randint(0, 9)
		row = random.randint(0, 9)

		# If the coordinates point to an empty field, deploy the ship - else, reprompt the computer
		if mapa[row][column] == 0:
			mapa[row][column] = 2
			print(f"Ship no. {i} has been deployed!")
			sleep(1)
		else:
			i -= 1

		i += 1


def battle(mapa):
	"""As long as both the user and the computer have ships on the map, they take turns in order to hit eachother's ships."""

	# At the begining of the battle, both the user and the computer have 5 ships on the map."""
	user = 5
	computer = 5

	while user > 0 and computer > 0:
		print("YOUR TURN!\n")
		
		# Handling improper input from the user for the X coordinate
		try:
			column = int(input("Enter the X coordinate: "))
		except:
			column = -1

		if column < 0 or column > 9:
			while column < 0 or column > 9:
				try:
					column = int(input("The X coordinate must be a number between 0 and 9: "))
				except:
					column = -1	
		
		# Handling improper input from the user for the Y coordinate
		try:
			row = int(input(f"Enter the Y coordinate: "))
		except:
			row = -1

		if row < 0 or row > 9:
			while row < 0 or row > 9:
				try:
					row = int(input("The Y coordinate must be a number between 0 and 9: "))
				except:
					row = -1	

		print()
		
		# VALUE LEGEND:

		# 0 - Empty field
        # 1 - Location of the user ship (print '@' on map)
        # 2 - Location of the computer ship (hidden from map)
        # 3 - Computer ship is sunk (print '!' on map)
        # 4 - User ship is sunk (print 'x' on map)
        # 5 - User missed (print '-' on map)
        # 6 - Computer missed (hidden from map)
		
		if mapa[row][column] == 1:
			mapa[row][column] = 3
			print("YOU SUNK YOUR OWN SHIP!\n")
			user -= 1
		elif mapa[row][column] == 2:
			mapa[row][column] = 4
			print("YOU SUNK THE COMPUTER'S SHIP!\n")
			computer -= 1
		elif mapa[row][column] == 3 or mapa[row][column] == 4:
			print("THAT SHIP HAS ALREADY BEEN SUNK!\n")		
		else:
			print("YOU MISSED!\n")
			mapa[row][column] = 5

		sleep(1)	

		print("COMPUTER'S TURN!\n")
		sleep(1)
		column = random.randint(0, 9)
		row = random.randint(0, 9)

		if mapa[row][column] == 1:
			mapa[row][column] = 3
			print("THE COMPUTER SUNK YOUR SHIP!\n")
			user -= 1
		elif mapa[row][column] == 2:
			mapa[row][column] = 4
			print("THE COMPUTER SUNK ITS OWN SHIP!\n")
			computer -= 1
		elif mapa[row][column] == 3 or mapa[row][column] == 4:
			pass		
		else:
			print("COMPUTER MISSED!\n")

		sleep(1)

		printMap(mapa)

		# Printing the current result at the end of each turn
		print(f"USER: {user} | COMPUTER: {computer}\n")	

	print("************************************\n")

	# Deciding and declaring the winner of the game
	if user > computer:
		print("CONGRATULATIONS! YOU ARE THE WINNER!")
	elif user < computer:
		print("THE COMPUTER WON!")
	else:
		print("IT'S A TIE!")	



if __name__=="__main__":
	main()