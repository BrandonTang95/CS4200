
import random

def is_solvable(board):
    
    # Check if a given 8-puzzle board is solvable
    # Count inversions to determine solvability
    
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions % 2 == 0

# Generates a random solvable 8-puzzle board configuration
def random_generator():
    board = list(range(9))
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return board

def main():
    # Generate 50 random test cases and write them to 'additional_test_cases.txt'
    with open('additional_test_cases.txt', 'w') as f:
        for _ in range(50):
            board = random_generator()
            f.write(' '.join(map(str, board)) + '\n')

if __name__ == "__main__":
    main()
