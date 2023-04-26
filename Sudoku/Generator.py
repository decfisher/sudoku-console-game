import copy
from random import shuffle

# Generates a new solved solution for a game of sudoku
class Generator:
    def __init__(self, diff_lvl):
        self.diff_lvl = diff_lvl
        self.board = self.reset_board()
        self.generate_solution(self.board)
        self.solution = copy.deepcopy(self.board)
        self.remove_nums()
        self.counter = 0

    def get_solution(self):
        return self.solution
    
    def get_puzzle(self):
        return self.board
    
    def reset_board(self):
        return [[0 for i in range(9)] for j in range(9)]

    def is_num_in_row(self, board, row, num):
        if num in board[row]:
            return True
        return False

    def is_num_in_col(self, board, col, num):
        for i in range(9):
            if board[i][col] == num:
                return True
        return False
    
    def is_num_in_subgrid(self, board, row, col, num):
        # Take the row and col, find floor division of 3 and multiply
        # by 3 to get subgrid coords for particular (row, col) i.e., sub row/col 0, 1 or 2
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3

        # Iterate through the subgrid to check if the number exists (remember zero-indexed)
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if board[i][j] == num:
                    return True
        return False

    # Check if number is in the same row, column or subgrid to align with constraints of sudoku
    def is_valid_num(self, board, row, col, num):
        if self.is_num_in_row(board, row, num):
            return False
        elif self.is_num_in_col(board, col, num):
            return False
        elif self.is_num_in_subgrid(board, row, col, num):
            return False
        return True
    
    def find_next_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return
    
    def generate_solution(self, board):
        # Valid numbers allowed on a sudoku board
        valid_nums = [1,2,3,4,5,6,7,8,9]

        for val in range(0, 81):
            # Get position values from value in range 0-80 (zero-indexed)
            row = val // 9 # Floor division to split up the rows e.g. 0-8 = 0, 9-17 = 1, and so on
            col = val % 9 # Modulus division to split for columns e.g. how many times n goes into 9 = column

            # Check position value is equal to zero, if not...
            if board[row][col] == 0:
                shuffle(valid_nums)
                for num in valid_nums:
                    if self.is_valid_num(board, row, col, num):
                        # If number is valid, insert it in position
                        board[row][col] = num
                        if not self.find_next_empty(board):
                            # If no more empty squares, generation is complete
                            return True
                        else:
                            # If there is empty squares, recursively continue with algorithm
                            if self.generate_solution(board):
                                return True
                            
                # If the number to be inserted is not valid, break from the loop
                break

        # ...make it equal to zero before continuing with algorithm, 
        # where it can determine if another number is valid
        board[row][col] = 0
        return False
    
    def solve(self, board):
        valid_nums = [1,2,3,4,5,6,7,8,9]

        for val in range(0, 81):
            row = val // 9
            col = val % 9

            # Check position value is equal to zero, if not...
            if board[row][col] == 0:
                shuffle(valid_nums) # Shuffle to pick random number selection
                for num in valid_nums:
                    if self.is_valid_num(board, row, col, num):
                        # If number is valid, insert it in position
                        board[row][col] = num
                        if not self.find_next_empty(board):
                            # If no more empty squares, solve is complete
                            self.counter += 1
                            break
                        else:
                            # If there is empty squares, recursively continue with algorithm
                            if self.solve(board):
                                return True
                            
                # If the number to be inserted is not valid, break from the loop
                break

        # ...make it equal to zero before continuing with algorithm, 
        # where it can determine if another number is valid
        board[row][col] = 0
        return False
    
    def find_filled(self, board):
        filled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    filled.append((i, j))
        shuffle(filled)
        return filled
    
    def remove_nums(self):
        filled = self.find_filled(self.board)
        filled_count = len(filled)

        while filled_count > self.diff_lvl:
            row, col = filled.pop()
            filled_count -= 1
            removed = self.board[row][col]
            self.board[row][col] = 0

            self.counter = 0
            board_copy = copy.deepcopy(self.board)
            self.solve(board_copy)

            if self.counter != 1:
                self.board[row][col] = removed
        return