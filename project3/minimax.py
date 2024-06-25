
class MiniMaxAgent:
    def __init__(self, depth):
        self.depth = depth
        self.x = []

    def set_depth(self, depth):
        self.depth = depth

    def action(self, board):
        alpha = -999999
        beta = 999999
        self.max(board, self.depth, alpha, beta, 0, 0)
        board = board.generate_successor('X', self.x[0], self.x[1])
        print("-------- AI -------")
        board.print_board()
        print(f"AI move: {chr(self.x[0] + 97)}{self.x[1] + 1}")
        print()
        return board

    def max(self, board, depth, alpha, beta, next_x, next_y):
        if depth == 0:
            return board.evaluation(next_x, next_y)

        children = board.get_children()
        value = -999999

        for child in children:
            min_val = self.min(board.generate_successor('X', child[0], child[1]), depth - 1, alpha, beta, child[0], child[1])
            if value < min_val:
                value = min_val
                self.x = child

            if value > alpha:
                alpha = value

            if alpha >= beta:
                break

        return value

    def min(self, board, depth, alpha, beta, next_x, next_y):
        if depth == 0:
            return board.evaluation(next_x, next_y)

        children = board.get_children()
        value = 999999

        for child in children:
            max_val = self.max(board.generate_successor('O', child[0], child[1]), depth - 1, alpha, beta, child[0], child[1])
            if max_val < value:
                value = max_val

            if value < beta:
                beta = value

            if alpha >= beta:
                break

        return value
