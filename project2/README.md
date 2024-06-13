
# N-Queens Problem

The N-Queen problem involves placing N chess queens on an N×N chessboard so that no two queens attack each other. The chess queens can attack in any direction: horizontal, vertical, and diagonal. This project focuses on solving the N-Queen problem for N=8 using local search algorithms.

## Algorithms Implemented

### Steepest-Ascent Hill Climbing
Hill climbing is a mathematical optimization technique that starts with an arbitrary solution to a problem and iteratively makes incremental changes to improve the solution. The algorithm continues until no further improvements can be found. In this project, the steepest-ascent variant of hill climbing is used, where the best neighboring state is chosen at each step without allowing sideways movements.

### MIN-CONFLICTS
The MIN-CONFLICTS algorithm is a heuristic search algorithm used for solving constraint satisfaction problems. It attempts to reduce the number of conflicts in the current state by selecting a variable and assigning it a value that minimizes conflicts. This process is repeated until a solution is found or a maximum number of steps is reached.

## Project Structure

- `board.py`: Contains functions for generating board configurations, calculating the number of attacking pairs, and displaying the board.
- `algorithms.py`: Implements the Steepest-Ascent Hill Climbing and MIN-CONFLICTS algorithms.
- `main.py`: Runs multiple instances of the N-Queen problem, collects data on the performance of the algorithms, and outputs sample puzzles and solutions.

## Implementation Analysis

### Steepest-Ascent Hill Climbing
- **Success Rate**: Approximately 15% for N=8.
- **Average Running Time**: 0.0008 seconds.
- **Average Search Cost**: 0.0008 seconds.

### MIN-CONFLICTS
- **Success Rate**: Approximately 28% for N=8.
- **Average Running Time**: 0.0392 seconds.
- **Average Search Cost**: 0.0392 seconds.

The Steepest-Ascent Hill Climbing algorithm has a lower success rate due to its limitation of not allowing sideways movements, which can lead to getting stuck in local optima. The MIN-CONFLICTS algorithm performs better by continuously minimizing conflicts, leading to a higher success rate and slightly higher running time.

## How to Compile and Run the Code

### Prerequisites
- Python 3.x

### Instructions

1. Clone the repository or download the source code.
2. Ensure that the following files are present in the same directory:
   - `board.py`
   - `algorithms.py`
   - `main.py`

3. Open a terminal and navigate to the directory containing the files.
4. Run the following command to execute the program:
   ```sh
   python main.py
