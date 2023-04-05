from random import shuffle

# Generates a new solved solution for a game of sudoku
class Generator:
    def __init__(self):
        self.board = self.reset_board()

    def get_board(self):
        return self.board
    
    def reset_board(self):
        return [[0 for i in range(9)] for j in range(9)]

    def is_num_in_row(self, row, num):
        if num in self.board[row]:
            return True
        return False

    def is_num_in_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return True
        return False
    
    def is_num_in_subgrid(self, row, col, num):
        # Take the row and col, find floor division of 3 and multiply
        # by 3 to get subgrid coords for particular (row, col) i.e., sub row/col 0, 1 or 2
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3

        # Iterate through the subgrid to check if the number exists (remember zero-indexed)
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if self.board[i][j] == num:
                    return True
        return False

    # Check if number is in the same row, column or subgrid to align with constraints of sudoku
    def is_valid_num(self, row, col, num):
        if self.is_num_in_row(row, num):
            return False
        elif self.is_num_in_col(col, num):
            return False
        elif self.is_num_in_subgrid(row, col, num):
            return False
        return True
    
    def find_next_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return
    
    def generate_solution(self):
        # Valid numbers allowed on a sudoku board
        valid_nums = [1,2,3,4,5,6,7,8,9]

        for val in range(0, 81):
            row = val // 9 # Floor division to split up the rows e.g. 0-8 = 0, 9-17 = 1, and so on
            col = val % 9 # Modulus division to split for columns e.g. how many times n goes into 9 = column

            # Check position value is equal to zero, if not...
            if self.board[row][col] == 0:
                shuffle(valid_nums)
                for n in valid_nums:
                    if self.is_valid_num(row, col, n):
                        # If number is valid, insert it in position
                        self.board[row][col] = n
                        if not self.find_next_empty():
                            # If no more empty squares, generation is complete
                            return True
                        else:
                            # If there is empty squares, recursively continue with algorithm
                            if self.generate_solution():
                                return True
                            
                # If the number to be inserted is not valid, break from the loop
                break

        # ...make it equal to zero before continuing with algorithm, 
        # where it can determine if another number is valid
        self.board[row][col] = 0
        return False

