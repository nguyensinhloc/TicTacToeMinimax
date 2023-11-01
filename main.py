# Import random module
import random

# Define the board as a list of 9 elements
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define the symbols for the players
X = "X"
O = "O"

# Define the possible winning combinations as a list of tuples
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
                        (0, 4, 8), (2, 4, 6)] # diagonal

# Define a function to print the board
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Define a function to check if the board is full
def is_full():
    return " " not in board

# Define a function to check if a player has won
def is_winner(player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Define a function to get the empty squares on the board
def get_empty_squares():
    return [i for i in range(9) if board[i] == " "]

# Define a function to make a move on the board
def make_move(square, player):
    board[square] = player

# Define a function to undo a move on the board
def undo_move(square):
    board[square] = " "

# Define a function to implement the Minimax algorithm with max_depth
def minimax(player, max_depth):
    # Base case: check if the game is over or the max depth is reached
    if is_winner(X):
        return (1, None) # X wins
    elif is_winner(O):
        return (-1, None) # O wins
    elif is_full():
        return (0, None) # Tie
    elif max_depth == 0:
        return (0, None) # No more moves to explore

    # Recursive case: loop through all the empty squares
    best_score = None
    best_move = None
    for square in get_empty_squares():
        # Make a move and evaluate it recursively with a reduced max depth
        make_move(square, player)
        score, _ = minimax(get_opponent(player), max_depth - 1)
        undo_move(square)

        # Update the best score and best move according to the player's turn
        if player == X: # X wants to maximize the score
            if best_score is None or score > best_score:
                best_score = score
                best_move = square
        else: # O wants to minimize the score
            if best_score is None or score < best_score:
                best_score = score
                best_move = square

    # Return the best score and best move for the current player
    return (best_score, best_move)

# Define a function to get the opponent of a player
def get_opponent(player):
    if player == X:
        return O
    else:
        return X

# Define a function to play the game with max_depth as an input parameter
def play(max_depth):
    # Print the initial board and instructions
    print_board()
    print("Welcome to Tic Tac Toe!")
    print("The board positions are numbered from 0 to 8 as follows:")
    print("0|1|2")
    print("-+-+-")
    print("3|4|5")
    print("-+-+-")
    print("6|7|8")

    # Loop until the game is over
    while True:
        # Get a valid move from X (randomly)
        while True:
            x_move = random.randint(0, 8)
            if board[x_move] == " ":
                break

        # Make the move and print the board
        make_move(x_move, X)
        print_board()

        # Check if X has won or tied
        if is_winner(X):
            print("X wins!")
            break
        elif is_full():
            print("It's a tie!")
            break

        # Get the best move from O using Minimax algorithm with max_depth
        _, o_move = minimax(O, max_depth)

        # Make the move and print the board
        make_move(o_move, O)
        print_board()

        # Check if O has won or tied
        if is_winner(O):
            print("O wins!")
            break
        elif is_full():
            print("It's a tie!")
            break

# Generate a random max_depth between 1 and 9
max_depth = random.randint(1, 9)

# Start the game with a random max_depth
play(max_depth)
