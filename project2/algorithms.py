
# algorithms.py
from board import generate_board, calculate_attacks
import random

def get_neighbors(board):
    
    # Generate all neighboring states of the current board configuration
    # Returns a list of neighboring board configurations
    
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if j != board[i]:
                neighbor = list(board)
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def steepest_ascent_hill_climbing(board):
    
    # Solve the N-Queen problem using steepest-ascent hill climbing
    # Returns a tuple of the final board configuration and number of attacks
    
    current_board = board
    current_attacks = calculate_attacks(current_board)
    while True:
        neighbors = get_neighbors(current_board)
        next_board = min(neighbors, key=calculate_attacks)
        next_attacks = calculate_attacks(next_board)
        if next_attacks >= current_attacks:
            return current_board, current_attacks
        current_board, current_attacks = next_board, next_attacks

def min_conflicts(board, max_steps=1000):
    
    # Solve the N-Queen problem using the MIN-CONFLICTS algorithm
    # Returns a tuple of the final board configuration and number of attacks
    
    n = len(board)
    for _ in range(max_steps):
        conflicts = calculate_attacks(board)
        if conflicts == 0:
            return board, conflicts
        
        col = random.choice([i for i in range(n) if calculate_attacks(board) > 0])
        min_conflicts = float('inf')
        best_row = None
        for row in range(n):
            board[col] = row
            conflicts = calculate_attacks(board)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_row = row
        board[col] = best_row
    return board, calculate_attacks(board)
