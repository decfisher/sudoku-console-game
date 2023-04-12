from Sudoku.Core import Core

def main():
    Core().play()

def exit_game():
    print("\nExiting game...")
    exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        exit_game()