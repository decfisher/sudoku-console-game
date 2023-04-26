from Sudoku.Generator import Generator

from Error.InvalidGuessException import InvalidGuessException

class Board:
    def __init__(self, diff_lvl):
        self.generator = self.generate_game_board(diff_lvl)
        self.puzzle = self.generator.get_puzzle()
        self.solution = self.generator.get_solution()

    def generate_game_board(self, diff_lvl):
        return Generator(diff_lvl)
    
    def get_current_progress(self):
        return self.puzzle
    
    def is_complete(self):
        return self.puzzle == self.solution
    
    def guess(self, x, y, num):
        # Revert input to zero-indexed coordinates, this allows players to guess the coordinates as seen 
        # but allows the program to read them properly
        row = x - 1
        col = y - 1

        # Check coordinates are valid within the bounds of sudoku
        if row not in range(0,9) or col not in range(0,9):
            raise InvalidGuessException(f'({x},{y}) is not a valid position on the board')

        # Check the number guess is within valid sudoku range
        if num not in range(1,10):
            raise InvalidGuessException(f'Your guess of {num} is not within the bounds of sudoku, valid number range is 1-9')
        
        # Check the grid does not already have a clue inserted at guessed position
        if self.puzzle[row][col] != 0:
            raise InvalidGuessException(f'Grid already has a clue at position ({x},{y})')

        # Add num to grid
        self.puzzle[row][col] = num

    def adjust_board(self, row, col, num):
        self.puzzle[row][col] = num

    def get_empty(self):
        empty_coords = []
        for row in range(0,9):
            for col in range(0,9):
                if self.puzzle[row][col] == 0:
                    empty_coords.append((row, col, self.solution[row][col]))
        return empty_coords
            