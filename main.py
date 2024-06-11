
import random
import os
from board import Board
from solver import Solver

def is_solvable(board):
    
    # Check if a given 8-puzzle board is solvable
    # Count inversions to determine solvability
    
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0:
                inversions += 1
    return inversions % 2 == 0



def random_generator():
    
    # Generate a random solvable 8-puzzle board
    
    board = list(range(9))
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return board



def read_file(file_name):
    
    # Read puzzles from a file
    # Each puzzle is represented by multiple lines
    # Convert the lines into a list of integers
    
    puzzles = []
    try:
        with open(file_name, 'r') as file:
            current_puzzle = []
            for line in file:
                line = line.strip()
                print(f"Reading line: {line}")  # Debug print statement
                if line and all(c.isdigit() or c.isspace() for c in line):
                    parts = line.split()
                    current_puzzle.extend(list(map(int, parts)))
                    if len(current_puzzle) == 9:
                        puzzles.append(current_puzzle)
                        current_puzzle = []
                else:
                    print(f"Skipping invalid line: {line}")  # Debug print statement
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return puzzles



def solve_board(board):
    
    # Solves the given board using both heuristics without documenting the result
    
    solver1 = Solver(Board(board), heuristic='h1')
    solver2 = Solver(Board(board), heuristic='h2')

    print(f"H1: {' -> '.join(solver1.solution_path)}")
    print(f"H2: {' -> '.join(solver2.solution_path)}")

    print(f"Runtime for H1: {solver1.run_time:.2f} ms")
    print(f"Runtime for H2: {solver2.run_time:.2f} ms")



def solve_and_document(board):
    
    # Solves the given board using both heuristics and documents the result
    
    solver1 = Solver(Board(board), heuristic='h1')
    solver2 = Solver(Board(board), heuristic='h2')

    print(f"H1: {' -> '.join(solver1.solution_path)}")
    print(f"H2: {' -> '.join(solver2.solution_path)}")

    print(f"Runtime for H1: {solver1.run_time:.2f} ms")
    print(f"Runtime for H2: {solver2.run_time:.2f} ms")

    document_results(board, solver1, solver2)

def document_results(board, solver1, solver2):
    
    # Writes the results of the solved puzzle to 'results.txt'
    
    with open('results.txt', 'a') as f:
        f.write(f"Initial State: {''.join(map(str, board))}\n")
        f.write(f"Heuristic Function: h1 (misplaced tiles)\n")
        f.write(f"- Search Cost: {solver1.search_cost}\n")
        f.write(f"- Depths: {solver1.solution_depth}\n")
        f.write(f"- Run Time: {solver1.run_time:.2f} ms\n")
        f.write('H1: ' + ' -> '.join(solver1.solution_path) + '\n')
        f.write("\n")
        f.write(f"Heuristic Function: h2 (Manhattan Distance)\n")
        f.write(f"- Search Cost: {solver2.search_cost}\n")
        f.write(f"- Depths: {solver2.solution_depth}\n")
        f.write(f"- Run Time: {solver2.run_time:.2f} ms\n")
        f.write('H2: ' + ' -> '.join(solver2.solution_path) + '\n')
        f.write("\n" + "-"*50 + "\n")



def main():
    
    # Main function to run the 8-puzzle solver program
    # Provides menu options for user interaction and handles puzzle solving
    
    # Sample puzzles with different solution depths
    sample_puzzles = [
        ([1, 2, 3, 4, 0, 5, 6, 7, 8], "< 6"),
        ([1, 2, 3, 4, 5, 6, 0, 7, 8], "between 6 and 12"),
        ([8, 6, 7, 2, 5, 4, 3, 0, 1], "> 12")
    ]

    for puzzle, depth in sample_puzzles:
        print("\n")
        print(f"Solving sample puzzle with solution depth {depth}: {puzzle}")
        solve_board(puzzle)
    
    print("\n")
    
    while True:
        choice = int(input("Select an option:\n1. Input a specific 8-puzzle configuration\n2. Generate random 8-puzzle problem\n3. Read 8-puzzle input from file\n4. Quit\n"))

        if choice == 1:
            board = list(map(int, input("Enter the 8-puzzle configuration (use space to separate numbers, 0 for blank, e.g., '1 2 3 4 5 6 7 8 0'): ").strip().split()))
            if is_solvable(board):
                print(f"Solving puzzle: {board}")
                solve_and_document(board)
                print("\n")
            else:
                print("The puzzle is not solvable.")
                print("\n")
                
        elif choice == 2:
            board = random_generator()
            print(f"Solving random puzzle: {board}")
            solve_board(board)
            print("\n")
            
        elif choice == 3:
            print("Ensure your input file is formatted as follows (one puzzle per line, numbers separated by spaces):")
            print("Example:")
            print("1 2 3 4 0 5 6 7 8")
            print("8 7 6 5 4 3 2 1 0")
            file_name = input("Enter the name of the test file (the file must be in the same directory as this program): ")
            if os.path.isfile(file_name):
                puzzles = read_file(file_name)
                if puzzles:
                    for puzzle in puzzles:
                        if len(puzzle) == 9:  # Ensure the puzzle has exactly 9 tiles
                            board = puzzle
                            print(f"Solving puzzle: {board}")
                            solve_and_document(board)
                        else:
                            print(f"Invalid puzzle format (not 9 tiles): {puzzle}")
                    print("All puzzles from the file have been processed. Results have been saved to 'results.txt'.")
                else:
                    print("No puzzles found or an error occurred while reading the file.")
            else:
                print("The file does not exist or is not in the same directory as the program.")
        elif choice == 4:
            print("Quitting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
