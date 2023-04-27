def welcome_splash():
    print("_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~.")
    print("   _____ _    _     _       _          ")
    print("  / ____| |  | |   | |     | |         ")
    print(" | (___ | |  | | __| | ___ | | ___   _ ")
    print("  \___ \| |  | |/ _` |/ _ \| |/ / | | |")
    print("  ____) | |__| | (_| | (_) |   <| |_| |")
    print(" |_____/ \____/ \__,_|\___/|_|\_\\\\__,_|\n")
    print("_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~.")
    print("\n            Welcome to Sudoku!")
    print("\n🚨 If application is closed, save data will be lost! 🚨")

def menu_list():
    print("\nMAIN MENU")
    print("1. Play new game")
    print("2. Replay a game")
    print("3. Exit")

def diff_list():
    print("\nCHOOSE DIFFICULTY")
    print("1. Easy 🟢")
    print("2. Medium 🟠")
    print("3. Hard 🔴")

def guess_options():
    print("\nCHOOSE ACTION")
    print("1. Submit guess")
    print("2. Undo")
    print("3. Redo")
    print("4. Check board (1x 🪙)")
    print("5. Get hint (3x 🪙)")
    print("6. Show remaining numbers")

def print_grid(grid_arr):
    # Taken from a StackOverflow thread
    # Response by Blckknght [https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3]
    print("\n+" + "---+" * 9)
    for i, row in enumerate(grid_arr):
        print(("|" + " {}   {}   {} |" * 3).format(* [x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+" * 9)
        else:
            print("+" + "   +" * 9)

def print_mistakes(mistakes):
    if mistakes == 0:
        print("\n✅ No mistakes found!")
    elif mistakes == 1:
        print("\n❌ Your board has 1 mistake!")
    else:
        print(f'\n❌ Your board has {mistakes} mistakes!')

def print_remaining_nums(nums: dict):
    keys = sorted(nums.keys())
    nums_to_print = dict()
    for k in keys:
        if nums.get(k) != 0:
            nums_to_print[k] = nums.get(k)
    print(f'\n🔢 NUMBERS LEFT: {nums_to_print}')

def print_hint(row, col, value):
    print(f'\n💡 HINT (ROW: {row + 1}, COL: {col + 1}, CLUE: {value})')

def print_saves(saves):
    print("\nCHOOSE SAVE")
    for index, save in enumerate(saves):
        print(f'{index + 1}. Game {index + 1}') 