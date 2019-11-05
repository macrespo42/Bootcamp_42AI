import random
import sys

nb_to_guess = random.randrange(1, 100)
game = True
turn = 1
print("This is an interactive guessing game!")
print("You have to guess a number between 1 and 99 enter 'exit' for leave")
while (game == True):
	response = input("What's your guess between 1 and 99?\n")
	if (response == "exit"):
		print("Goodbye !")
		sys.exit(0)
	else:
		try:
			response = int(response)
		except ValueError:
			print("bad input, bye")
			sys.exit(0)
	if (response > nb_to_guess):
		print("Too high !")
	elif (response < nb_to_guess):
		print("Too low !")
	else:
		game = False
		if(response == 42):
			print("The answer to the ultimate question !")
		elif (turn == 1):
			print("Congratulations! You got it on your first try!")
		else:
			print("Congrats you got it in {} attemps".format(turn))
	turn += 1
