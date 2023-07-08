#This is a basic Tic-Tac-Toe game with an AI opponent to play against
import random

#Function to print the tic-tac-toe board
def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i * 3 + j], end=" ")
            print("|", end=" ")
        print("\n---------")

#Check if player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

#Make player's move
def make_move(board, position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False

#Get the AI's move
def get_ai_move(board):
    #Check for a winning move
    for i in range(9):
        if board[i] == " ":
            board_copy = board[:]
            board_copy[i] = "O"
            if check_winner(board_copy, "O"):
                return i

    #Check for a blocking move
    for i in range(9):
        if board[i] == " ":
            board_copy = board[:]
            board_copy[i] = "X"
            if check_winner(board_copy, "X"):
                return i

    #Choose a random move
    empty_positions = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_positions)

#Check if board is full
def is_board_full(board):
    return " " not in board

#Main game loop
def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        #Player's move
        position = int(input("Enter your move (0-8): "))
        if not make_move(board, position, "X"):
            print("Invalid move! Try again.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        #AI's move
        print("AI's turn...")
        position = get_ai_move(board)
        make_move(board, position, "O")

        print_board(board)

        if check_winner(board, "O"):
            print("Sorry, you lost!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

#Start the game
play_game()
