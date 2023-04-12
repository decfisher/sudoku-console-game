from random import randrange

from Error.PlayerInputParseException import PlayerInputParseException

from helpers.display import *
from Sudoku.Board import *

class Core:
	def __init__(self):
		self.diff_lvl = 0
		self.board = None

	def play(self):
		welcome_splash()
		self.menu()

	def menu(self):
		menu_list()
		while True:
			try:
				usrChoice = int(input("Choose an option: "))
				if usrChoice == 1:
					self.diff_lvl = self.choose_diff()
					self.board = Board(self.diff_lvl)
					while True:
						if self.board.get_mistakes() > 3:
							print("\nGame over! You have made too many mistakes!")
							break
						if self.board.is_complete():
							print_grid(self.board.get_current_progress())
							print("\nYou completed the board, well done!")
							break
						self.make_guess()
					break
				if usrChoice == 2:
					print("Bye bye!")
					break
				else:
					print("Invalid choice!")
			except ValueError:
				print("Problem accepting your input, try again!")
				continue

	def choose_diff(self):
		diff_list()
		while True:
			try:
				self.diff_lvl = int(input("Choose an option: "))
				if self.diff_lvl == 1:
					print("\nStarting an easy game...")
					return randrange(36, 41)
				if self.diff_lvl == 2:
					print("\nStarting a medium game...")
					return randrange(32, 35)
				if self.diff_lvl == 3:
					print("\nStarting a hard game...")
					return randrange(28, 31)
				else:
					print("Choose a valid game mode")
			except ValueError:
				print("Problem accepting your input, try again!")
				continue

	def make_guess(self):
		while True:
			try:
				print_grid(self.board.get_current_progress())
				print(f'\nMistakes: {self.board.get_mistakes()}/3')
				row, col, num = self.parse_guess_input(input("\nEnter guess (row,col,num): "))
				return self.board.player_guess(row, col, num)
			except Exception as e:
				print(str(e))
				continue

	def parse_guess_input(self, guess: str):
		vals = guess.split(",")
		try:
			player_input = tuple([int(v) for v in vals])
			if len(player_input) > 3:
				raise PlayerInputParseException
			return player_input
		except ValueError:
			raise PlayerInputParseException