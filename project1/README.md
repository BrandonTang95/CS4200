### README for 8-Puzzle Solver

---

## Artificial Intelligence Game: 8-puzzle

### Algorithm
This project uses the A* algorithm with two different heuristic functions to solve the 8-puzzle problem efficiently.

---

### File Descriptions
- **main.py**: Contains the main function with three different menu options for user interaction.
- **board.py**: Contains the Board class which manages the board information and operations.
- **solver.py**: Contains the Solver class which implements the A* algorithm using the h1 heuristic (number of misplaced tiles).
- **generate_test_cases.py**: Generates random solvable 8-puzzle configurations for testing purposes.

---

### Approach

#### a. User Selection
The user interface provides three menu options:
1. Input a specific 8-puzzle configuration.
2. Generate a random 8-puzzle problem.
3. Read 8-puzzle input from a file.

#### b. Data Structure
To improve performance and speed:
- A 1-dimensional array of integers is used instead of a 2-dimensional array.

#### c. Heuristic Functions
1. **h1**: Number of misplaced tiles.
   - A for loop checks if each tile is in the correct position.
2. **h2**: Sum of the Manhattan distances of the tiles from their goal positions.
   - The Manhattan distance is calculated as `|(i / 3) - (char[i] / 3)| + |(i % 3) - (char[i] % 3)|`.

#### d. Open Set and Closed Set
1. **Open Set**: The set of boards created but not yet considered.
   - Implemented as a priority queue sorted by the heuristic function and depth.
2. **Closed Set**: The set of boards already considered as solutions.
   - Implemented using a hash map to check if a new board has already been visited.

#### e. Search Cost
A counter increments each time a new child node is created.

#### f. Board and Node Information
1. **Board**: Contains only heuristic values.
2. **Node**: Each board is treated as a node, containing:
   - Moves (depth)
   - Previous node (parent)
   - The final depth for the goal state is the `moves` value of the final node.
   - The program follows the previous node information to print each step from the initial state to the final state.

---

### Analysis
By comparing the output results, the average search cost and run time for the A* algorithm using different heuristic functions (h1 and h2) are almost the same from depth 2 to depth 6. However, starting from depth 8, the average search cost and run time using h1 (number of misplaced tiles) increase more than those using h2 (Manhattan Distance). After depth 20, the average run time using h1 increases dramatically.

After testing 100+ random puzzles, it can be concluded that using the A* algorithm with h2 (Manhattan Distance) generates fewer nodes and costs less time to solve the 8-puzzle problem. Thus, the A* algorithm with the Manhattan Distance heuristic is more efficient.

---

### Compilation and Execution Instructions

#### Requirements
- Python 3.x
- Required libraries: `heapq`, `time`

#### Steps to Compile and Run

1. **Generate Test Cases**
   - Run `generate_test_cases.py` to create random test cases.
     ```bash
     python generate_test_cases.py
     ```

2. **Run the Main Program**
   - Execute `main.py` to start the 8-puzzle solver program.
     ```bash
     python main.py
     ```

3. **User Interface**
   - Follow the on-screen prompts to:
     - Input a specific 8-puzzle configuration.
     - Generate a random 8-puzzle problem.
     - Read 8-puzzle inputs from a file. Ensure the input file is formatted correctly and located in the same directory as the program.

#### Example Input File Format
Ensure your input file is formatted as follows (one puzzle per line, numbers separated by spaces):
```
1 2 3 4 0 5 6 7 8
8 7 6 5 4 3 2 1 0
```

#### Output
- The results of solving puzzles will be saved to `results.txt`.
- Each result will include:
  - Initial state
  - Heuristic function used
  - Search cost
  - Solution depth
  - Run time
  - Solution path


### Additional Information

For more details about the project implementation, including the A* algorithm and heuristic functions, refer to the comments and documentation within the source code files.
