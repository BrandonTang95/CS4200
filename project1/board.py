
class Board:
    
    # Initialize a Board with a given configuration
    def __init__(self, board_array):
        self.board_array = board_array
        self.zero = self.board_array.index(0)
        self.h1 = self.calculate_h1
        self.h2 = self.calculate_h2

    # Calculate the heuristic h1: the number of misplaced tiles
    @property
    def calculate_h1(self):
        # Number of misplaced tiles
        return sum(1 for i in range(len(self.board_array)) if self.board_array[i] != 0 and self.board_array[i] != i)

    # Calculate the heuristic h2: the sum of all the Manhattan distances of the tiles from their goal positions
    @property
    def calculate_h2(self):
        # Manhattan distance
        return sum(abs(i // 3 - self.board_array[i] // 3) + abs(i % 3 - self.board_array[i] % 3)
                   for i in range(len(self.board_array)) if self.board_array[i] != 0)

    # Check if the current board is the goal state
    def is_goal(self):
        return self.board_array == list(range(9))

    # Generate all valid neighboring board configurations
    def neighbors(self):
        neighbor_boards = []
        zero_index = self.zero
        row, col = divmod(zero_index, 3)
        moves = {'up': -3, 'down': 3, 'left': -1, 'right': 1}
        for direction, move in moves.items():
            new_zero_index = zero_index + move
            if (direction == 'up' and row > 0) or (direction == 'down' and row < 2) or \
               (direction == 'left' and col > 0) or (direction == 'right' and col < 2):
                new_board = self.board_array[:]
                new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
                neighbor_boards.append(Board(new_board))
        return neighbor_boards

    # Convert the board configuration to a string representation
    def to_string(self):
        return ''.join(map(str, self.board_array))

    # Check if two boards are equal based on their configurations
    def __eq__(self, other):
        return self.board_array == other.board_array

    # Returns the hash of the node based on its board configuration
    def __hash__(self):
        return hash(tuple(self.board_array))

    # Compare two nodes based on their cost using h1 heuristic
    def __lt__(self, other):
        return (self.h1 + self.h2) < (other.h1 + other.h2)
