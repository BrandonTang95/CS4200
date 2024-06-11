
import heapq
import time
from board import Board

class Solver:
    # Initialize the Solver with the initial board configuration and heuristic
    def __init__(self, initial_board, heuristic='h1'):
        self.initial_board = initial_board
        self.heuristic = heuristic
        self.frontier = []
        self.explored = set()
        self.solution_depth = 0
        self.search_cost = 0
        self.run_time = 0
        self.solution_path = []
        self.solve()
        
    
    # Solves the 8-puzzle problem using A*
    def solve(self):
        start_time = time.time()
        initial_node = Node(self.initial_board)
        heapq.heappush(self.frontier, (initial_node.cost(self.heuristic), initial_node))

        while self.frontier:
            _, current_node = heapq.heappop(self.frontier)
            if current_node.board.is_goal():
                self.solution_depth = current_node.moves
                self.run_time = (time.time() - start_time) * 1000  # in milliseconds
                self.print_solution(current_node)
                return
            self.explored.add(current_node)

            for neighbor in current_node.board.neighbors():
                neighbor_node = Node(neighbor, current_node)
                if neighbor_node not in self.explored:
                    self.search_cost += 1
                    heapq.heappush(self.frontier, (neighbor_node.cost(self.heuristic), neighbor_node))
                    
                    
    # Prints the solution path from initial path to goal state
    def print_solution(self, node):
        path = []
        while node:
            path.append(node.board.to_string())
            node = node.parent
        self.solution_path = list(reversed(path))
        print(' -> '.join(self.solution_path))


class Node:
    # Initializes a Node with a board configuration and its parent node
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.moves = parent.moves + 1 if parent else 0

    # Calculate the cost of the node using the specified heuristic
    def cost(self, heuristic):
        return self.moves + (self.board.h1 if heuristic == 'h1' else self.board.h2)

    # Check if two nodes are equal based on their board configuration
    def __eq__(self, other):
        return self.board == other.board

    # Returns the hash of the node based on its board configuration
    def __hash__(self):
        return hash(self.board)

    # Compare two nodes based on their cost using h1 heuristic
    def __lt__(self, other):
        return self.cost('h1') < other.cost('h1')
