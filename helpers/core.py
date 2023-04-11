from random import randrange

from helpers.display import *
from Sudoku.Board import *

board: Board

def play():
    welcome_splash()
    menu()

def menu():
	menu_list()
	while True:
		try:
			usrChoice = int(input("Choose an option: "))
			if usrChoice == 1:
				diff_lvl = choose_diff()
				board = Board(diff_lvl)
				while not board.is_complete():
					make_guess(board)
				break
			if usrChoice == 2:
				print("Bye bye!")
				break
			else:
				print("Invalid choice!")
		except ValueError:
			print("Problem accepting your input, try again!")
			continue

def choose_diff():
	diff_list()
	while True:
		try:
			diff_lvl = int(input("Choose an option: "))
			if diff_lvl == 1:
				print("\nStarting an easy game...")
				return randrange(36, 41)
			if diff_lvl == 2:
				print("\nStarting a medium game...")
				return randrange(32, 35)
			if diff_lvl == 3:
				print("\nStarting a hard game...")
				return randrange(28, 31)
			else:
				print("Choose a valid game mode")
		except ValueError:
			print("Problem accepting your input, try again!")
			continue

def make_guess(board: Board):
	while True:
		try:
			print_grid(board.get_current_progress())
			row, col, num = parse_guess_input(input("Enter guess (row,col,num): "))
			board.player_guess(row, col, num)
		except Exception as e:
			print(str(e))
			continue

def parse_guess_input(guess: str):
	vals = guess.split(",")
	try:
		player_input = tuple([int(v) for v in vals])
		return player_input
	except ValueError:
		print("Problem accepting your input, try again!")
