import copy
from random import randrange, shuffle
from Sudoku.CreditHandler import CreditHandler
from Sudoku.GameSave import GameSave

from helpers.display import *
from Sudoku.Board import *

from Error.BoardManipulationException import BoardManipulationException
from Error.PlayerInputParseException import PlayerInputParseException
from Error.InvalidCreditsException import InvalidCreditsException

class Core:
	def __init__(self):
		self.diff_clues = 0
		self.board = None
		self.init_puzzle = []
		self.saves = GameSave()
		self.moves = []
		self.undo_stack = []
		self.redo_stack = []
		self.account = None

	def play(self):
		welcome_splash()
		self.menu()

	def reset(self):
		self.diff_clues = 0
		self.board = None
		self.moves = []
		self.undo_stack = []
		self.redo_stack = []
		self.account = None
		self.init_puzzle = []

	def menu(self):
		while True:
			try:
				menu_list()
				choice = int(input("\nChoose an option: "))
				if choice == 1:
					self.diff_clues = self.choose_diff()
					print("✅ Game board generated!")
					self.board = Board(diff_clues=self.diff_clues)
					self.account = CreditHandler(self.diff_clues)
					self.init_puzzle = copy.deepcopy(self.board.get_current_progress())
					self.execute_game()
					self.saves.save(self.moves, self.diff_clues, self.init_puzzle, self.board.solution)
					self.reset()
					continue
				if choice == 2:
					game_saves = self.saves.get_all_saves()
					if len(game_saves) < 1:
						print("\n❌ No previous games to load!")
						continue
					self.choose_save(game_saves)
					self.execute_game()
					continue
				if choice == 3:
					print("Bye bye 👋")
					break
				else:
					print("\n❌ Invalid choice!")
			except ValueError:
				print("\n❌ Problem accepting your input, try again!")
				continue

	def execute_game(self):
		while True:
			print(f'\n🪙 GAME CREDITS: {self.account.get_credits()}')
			print_grid(self.board.get_current_progress())
			if self.board.is_complete():
				print("\n✅ You completed the board, well done!")
				break
			self.move_options()
	
	def choose_save(self, saves: dict):
		print_saves(saves)
		while True:
			try:
				choice = int(input("\nChoose an option: "))
				if choice > len(saves) or choice < len(saves):
					print("\n❌ Invalid choice!")
					continue
				moves, clues, puzzle, solution = saves.get(choice)
				self.redo_stack = moves
				self.diff_clues = clues
				self.board = Board(puzzle=puzzle, solution=solution)
				self.account = CreditHandler(self.diff_clues)
				break
			except ValueError:
				print("\n❌ Problem accepting your input, try again!")
				continue


	def choose_diff(self):
		diff_list()
		while True:
			try:
				diff_lvl = int(input("\nChoose an option: "))
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
					print("\n❌ Choose a valid game mode")
			except ValueError:
				print("\n❌ Problem accepting your input, try again!")
				continue

	def move_options(self):
		guess_options()
		while True:
			try:
				option = int(input("\nChoose an option: "))
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
					print("\n❌ Choose a valid move option!")
			except InvalidGuessException as e:
				print(str(e))
				continue
			except ValueError:
				print("\n❌ Problem accepting your input, try again!")
				continue

	def make_guess(self):
		while True:
			try:
				row, col, num = self.parse_guess_input(input("\nEnter guess (row,col,num): "))
				self.undo_stack.append((row - 1, col - 1, num))
				self.redo_stack = []
				self.board.guess(row, col, num)
				self.account.bonus()
				self.moves.append((row - 1, col - 1, num))
				break
			except Exception as e:
				print(str(e))
				continue

	def parse_guess_input(self, guess: str):
		vals = guess.split(",")
		try:
			if len(vals) != 3:
				raise PlayerInputParseException(f'\n❌ Guess needs to be formatted as (row,col,num), expected 3 arguments and got {len(vals)}')
			player_input = tuple([int(v) for v in vals])
			return player_input
		except ValueError:
			raise PlayerInputParseException
		
	def undo_move(self):
		try:
			if not self.check_undo():
				raise BoardManipulationException("\n❌ No moves to undo!")
			row, col, num = self.undo_stack.pop()
			self.board.adjust_board(row, col, 0)
			self.redo_stack.append((row, col, num))
		except Exception as e:
			print(str(e))
	
	def redo_move(self):
		try:
			if not self.check_redo():
				raise BoardManipulationException("\n❌ No moves to redo!")
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
			self.account.spend(3)
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