class GameSave:
    def __init__(self):
        self.saves = dict()
        self.counter = 1
    
    def save(self, moves, diff_lvl, puzzle, solution):
        self.saves[self.counter] = (moves, diff_lvl, puzzle, solution)
        self.counter += 1

    def get_all_saves(self):
        return self.saves
