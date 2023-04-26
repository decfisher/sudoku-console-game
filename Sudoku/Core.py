from random import randrange, shuffle
from Sudoku.CreditHandler import CreditHandler

from helpers.display import *
from Sudoku.Board import *

from Error.BoardManipulationException import BoardManipulationException
from Error.PlayerInputParseException import PlayerInputParseException
from Error.InvalidCreditsException import InvalidCreditsException

class Core:
	def __init__(self):
		self.diff_lvl = 0
		self.board = None
		self.moves = []
		self.undo_stack = []
		self.redo_stack = []
		self.account = None

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
					print("✅ Game board generated!")
					self.board = Board(self.diff_lvl)
					while True:
						print(f'\n🪙 GAME CREDITS: {self.account.get_credits()}')
						print_grid(self.board.get_current_progress())
						if self.board.is_complete():
							print("\n✅ You completed the board, well done!")
							break
						self.move_options()
					self.menu()
					break
				if usrChoice == 2:
					print("Bye bye 👋")
					break
				else:
					print("❌ Invalid choice!")
			except ValueError:
				print("❌ Problem accepting your input, try again!")
				continue

	def choose_diff(self):
		diff_list()
		while True:
			try:
				self.diff_lvl = int(input("Choose an option: "))
				if self.diff_lvl == 1:
					print("\nStarting an easy game...")
					self.account = CreditHandler(6, self.diff_lvl)
					return randrange(36, 41)
				if self.diff_lvl == 2:
					print("\nStarting a medium game...")
					self.account = CreditHandler(4, self.diff_lvl)
					return randrange(32, 35)
				if self.diff_lvl == 3:
					print("\nStarting a hard game...")
					self.account = CreditHandler(2, self.diff_lvl)
					return randrange(28, 31)
				else:
					print("❌ Choose a valid game mode")
			except ValueError:
				print("❌ Problem accepting your input, try again!")
				continue

	def move_options(self):
		guess_options()
		while True:
			try:
				option = int(input("Choose an option: "))
				if option == 1:
					self.make_guess()
					break
				if option == 2:
					self.undo_move()
					break
				if option == 3:
					self.redo_move()
					break
				if option == 4:
					self.compare_board()
					break
				if option == 5:
					self.give_hint()
					break
				if option == 6:
					self.nums_left()
					break
				else:
					print("❌ Choose a valid move option!")
			except InvalidGuessException as e:
				print(str(e))
				continue
			except ValueError:
				print("❌ Problem accepting your input, try again!")
				continue

	def make_guess(self):
		while True:
			try:
				row, col, num = self.parse_guess_input(input("\nEnter guess (row,col,num): "))
				self.undo_stack.append((row - 1, col - 1, num))
				self.redo_stack = []
				self.board.guess(row, col, num)
				self.account.bonus()
				break
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
		
	def undo_move(self):
		try:
			if not self.check_undo():
				raise BoardManipulationException("\n❌ No moves to undo!")
			self.account.spend(1)
			row, col, num = self.undo_stack.pop()
			self.board.adjust_board(row, col, 0)
			self.redo_stack.append((row, col, num))
		except Exception as e:
			print(str(e))
	
	def redo_move(self):
		try:
			if not self.check_redo():
				raise BoardManipulationException("\n❌ No moves to redo!")
			self.account.spend(1)
			row, col, num = self.redo_stack.pop()
			self.board.adjust_board(row, col, num)
			self.undo_stack.append((row, col, num))
		except Exception as e:
			print(str(e))
	
	def check_undo(self):
		if len(self.undo_stack) == 0:
			return False
		return True
	
	def check_redo(self):
		if len(self.redo_stack) == 0:
			return False
		return True
	
	def compare_board(self):
		total_mistakes = 0
		try:
			self.account.spend(1)
			for row in range(0,9):
				for col in range(0,9):
					if self.board.puzzle[row][col] == 0:
						continue
					if self.board.puzzle[row][col] != self.board.solution[row][col]:
						total_mistakes += 1
			print_mistakes(total_mistakes)
			return total_mistakes
		except InvalidCreditsException as e:
			print(str(e))
			return 0
	
	def give_hint(self):
		try:
			self.account.spend(2)
			clues = self.board.get_empty()
			shuffle(clues)
			row, col, value = clues.pop()
			print_hint(row, col, value)
			return (row, col, value)
		except InvalidCreditsException as e:
			print(str(e))
	
	def nums_left(self):
		nums = dict()
		for row in range(0,9):
			for col in range(0,9):
				board_val = self.board.puzzle[row][col]
				if board_val == self.board.solution[row][col]:
					nums[board_val] = nums.get(board_val, 9) - 1
		print_remaining_nums(nums)
		return nums