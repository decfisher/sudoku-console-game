from helpers.display import *

from Sudoku.Generator import *

generator = Generator()

empty_board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

counter = 0

def play():
    welcome_splash()
    menu()

def menu():
	menu_list()
	while True:
		try:
			usrChoice = int(input("Choose an option: "))
			if usrChoice == 1:
				generator.generate_solution()
				print_grid(generator.get_board())
				break
			if usrChoice == 2:
				print("Bye bye")
				break
			else:
				print("Invalid choice!")
		except ValueError:
			print("Problem accepting your input, try again!")
			continue

