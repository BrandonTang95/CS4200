
# main.py
import time
from board import generate_board, display_board
from algorithms import steepest_ascent_hill_climbing, min_conflicts

def solve_n_queen_instances(n, algorithm, num_instances=100):
    
    # Run multiple instances of the N-Queen problem and collect data
    # Displays success rate, average run time, and average search cost
    
    solved_count = 0
    total_time = 0
    search_costs = []
    
    for _ in range(num_instances):
        initial_board = generate_board(n)
        start_time = time.time()
        if algorithm == "hill_climbing":
            solution_board, attacks = steepest_ascent_hill_climbing(initial_board)
        elif algorithm == "min_conflicts":
            solution_board, attacks = min_conflicts(initial_board)
        end_time = time.time()
        
        if attacks == 0:
            solved_count += 1
        total_time += (end_time - start_time)
        search_costs.append(end_time - start_time)
    
    success_rate = (solved_count / num_instances) * 100
    average_time = total_time / num_instances
    average_cost = sum(search_costs) / num_instances
    
    print(f"{algorithm} - Solved: {solved_count}/{num_instances} ({success_rate}%)")
    print(f"Average Running Time: {average_time:.4f} seconds")
    print(f"Average Search Cost: {average_cost:.4f} seconds")

if __name__ == "__main__":
    n = 8
    num_instances = 100

    print("Testing Steepest-Ascent Hill Climbing Algorithm:")
    solve_n_queen_instances(n, "hill_climbing", num_instances)

    print("\nTesting MIN-CONFLICTS Algorithm:")
    solve_n_queen_instances(n, "min_conflicts", num_instances)

    # Output sample puzzles and solutions
    print("\nSample Puzzles and Solutions:")
    for _ in range(3):
        initial_board = generate_board(n)
        solution_board, attacks = steepest_ascent_hill_climbing(initial_board)
        print("Initial Board (Hill Climbing):")
        display_board(initial_board)
        print("Solution Board (Hill Climbing):")
        display_board(solution_board)

        initial_board = generate_board(n)
        solution_board, attacks = min_conflicts(initial_board)
        print("Initial Board (MIN-CONFLICTS):")
        display_board(initial_board)
        print("Solution Board (MIN-CONFLICTS):")
        display_board(solution_board)
