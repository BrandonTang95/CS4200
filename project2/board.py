
# board.py
import random

def generate_board(n):
    
    # Generate a random initial board configuration
    
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_attacks(board):
    
    # Calculate the number of attacking pairs of queens on the board
    
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def display_board(board):
    
    # Display the board configuration
    
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")
