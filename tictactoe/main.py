#
# A tic-tac-toe game!
#
import random
import sys


# The map of the game.
def display_game(game_map):
    for n in range(len(game_map)):
        print(f"{'|'.join(game_map[n])}")


# Ask to play or to play again after a game is finished
def start_game(start_or_play):
    while True:
        if start_or_play == 1:
            check = input("Are you ready to play? (Y/N) ").lower()
        else:
            check = input("Do you want to play again? (Y/N) ").lower()
        if check == 'y':
            print("Player 1 is X, Player 2 is O.")
            return
        elif check == 'n':
            print("Goodbye!")
            sys.exit()
        else:
            print("Please type Y for yes or N for no.")


# Prompts the player to choose a slot.
def player_choice():
    while True:
        check_for_int = 'string'
        while not check_for_int.isdigit():  # Checking for integer and not a string.
            check_for_int = input("Choose a slot by entering a value from 1-9: ")
            if check_for_int == 'exit':
                print("Player resigns!")
                exit()
            elif not check_for_int.isdigit():
                print("Invalid entry. Try again.")

        # The number is an integer but needs to be checked for range.
        choice_int = int(check_for_int)
        if choice_int in range(1, 10):
            if (board_game[int((choice_int-1)/3)][(choice_int-1) % 3]) in ['X', 'O']:
                print("Slot filled.")
            else:
                print(f"You've chosen {choice_int}")
                return choice_int
        else:
            print("Please enter a value from 1-9!")


# Places X or O on the map.
def player(chc, player_turn):
    x_and_o = ''
    if player_turn == 1:
        x_and_o = 'X'
    elif player_turn == 2:
        x_and_o = 'O'
    index = chc - 1
    board_game[int(index/3)][index % 3] = x_and_o
    display_game(board_game)
    return 1


# Checks if there's a win.
def win(letter):
    # Row checking
    for row in board_game:
        if all(cell == letter for cell in row):
            return 1 if letter == 'X' else 2

    # Column checking
    for col in range(len(board_game)):
        if all(board_game[row][col] == letter for row in range(len(board_game))):
            return 1 if letter == 'X' else 2

    # Diagonal checking
    if all(board_game[n][n] == letter for n in range(len(board_game))):
        return 1 if letter == 'X' else 2
    if all(board_game[n][2-n] == letter for n in range(len(board_game))):
        return 1 if letter == 'X' else 2

    return 0


# Initialize the game.
print("Welcome to a game of Tic, Tac and Toe!")
start_game(1)

# Main game loop.
while True:
    WINNER = 0
    TURN = random.randint(1, 2)
    board_game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    display_game(board_game)

    # Loop for turns, player 1 - player 2.
    while WINNER == 0:
        if TURN == 1:
            print("Player 1.")
            CHOICE = player_choice()
            TURN = player(CHOICE, 1) + 1
            WINNER = win('X')
        elif TURN == 2:
            print("Player 2.")
            CHOICE = player_choice()
            TURN = player(CHOICE, 2)
            WINNER = win('O')
    # Ask for a repeat.
    print(f'Player {WINNER} won!')
    start_game(2)
