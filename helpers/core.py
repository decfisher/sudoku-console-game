from helpers.display import *

def play():
    welcome_splash()
    menu()

def menu():
    menu_list()
    while True:
        try:
            usrChoice = int(input("Choose an option: "))
            if usrChoice == 1:
                print("Playing the game...")
                break
            if usrChoice == 2:
                print("Exiting the game...")
                break
            else:
                print("Please enter a valid choice!")
        except ValueError:
            print("Problem accepting your input, please try again!")
            continue