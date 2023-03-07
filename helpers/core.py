from helpers.display import *

starting_grid = [
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

def play():
    welcome_splash()
    menu()

def menu():
    menu_list()
    while True:
        try:
            usrChoice = int(input("Choose an option: "))
            if usrChoice == 1:
                print("Playing the game...\n")
                print_grid(starting_grid)
                break
            if usrChoice == 2:
                print("Exiting the game...")
                break
            else:
                print("Please enter a valid choice!")
        except ValueError:
            print("Problem accepting your input, please try again!")
            continue

def print_grid(grid_arr):
    # Taken from a StackOverflow thread, response by Blckknght [https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3]
    print("+" + "---+" * 9)
    for i, row in enumerate(grid_arr):
        print(("|" + " {}   {}   {} |" * 3).format(* [x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+" * 9)
        else:
            print("+" + "   +" * 9)
    print("\n")