from Error.InvalidGuessException import InvalidGuessException
from Sudoku.Generator import Generator

class Board:
    def __init__(self, diff_lvl):
        self.generator = self.generate_game_board(diff_lvl)
        self.puzzle = self.generator.get_puzzle()
        self.solution = self.generator.get_solution()

    def get_current_progress(self):
        return self.puzzle
    
    def is_complete(self):
        return self.puzzle == self.solution

    def generate_game_board(self, diff_lvl):
        return Generator(diff_lvl)
    
    def player_guess(self, row, col, num):
        if num == self.solution[row][col]:
            self.puzzle[row][col] = num
        else:
            raise InvalidGuessException(f'{num} is not valid at position {row}, {col}')