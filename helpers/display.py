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

def menu_list():
    print("\nMAIN MENU")
    print("1. Play new game")
    print("2. Exit")

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