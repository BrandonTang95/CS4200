
import copy
from score_point import PointScore

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.board = [['-' for _ in range(self.cols)] for _ in range(self.rows)]

    def clone(self):
        new_board = Board()
        new_board.board = copy.deepcopy(self.board)
        return new_board

    def generate_successor(self, c, row, col):
        new_board = self.clone()
        new_board.board[row][col] = c
        return new_board

    def print_board(self):
        print("-------------------")
        print("  ", end="")
        for col_counter in range(1, self.rows + 1):
            print(f"{col_counter} ", end="")
        print()

        for i in range(self.rows):
            print(f"{chr(i + 97)} ", end="")
            for j in range(self.cols):
                print(f"{self.board[i][j]} ", end="")
            print()
        print("-------------------")

    def is_goal(self, c):
        find = c * 4

        # Check rows
        for i in range(self.rows):
            if find in ''.join(self.board[i]):
                return True

        # Check columns
        for j in range(self.cols):
            col = ''.join(self.board[i][j] for i in range(self.rows))
            if find in col:
                return True

        return False

    def get_children(self):
        children = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == '-':
                    children.append([i, j])
        return children

    def has_neighbor(self, x, y):
        distance = 2
        for i in range(x - distance, x + distance + 1):
            if 0 <= i < self.rows and i != x and self.board[i][y] != '-':
                return True
        for j in range(y - distance, y + distance + 1):
            if 0 <= j < self.cols and j != y and self.board[x][j] != '-':
                return True
        return False

    def evaluation(self, X, Y):
        result = 0
        point_score = PointScore()
        if self.board[X][Y] == 'X':
            result = point_score.score_point(self.board, X, Y, 'X')
        elif self.board[X][Y] == 'O':
            result = point_score.score_point(self.board, X, Y, 'O') * -1
        return result

    def input_check(self, row, col):
        if col > 7 or row > 7:
            return False
        if self.board[row][col] != '-':
            print("error")
            return False
        return True

    def is_draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == '-':
                    return False
        return True

    def killer_check(self):
        x = 'X'
        move = 0

        killer_cases = [
            f"-{x}{x}{x}-",
            f"{x}{x}{x}-",
            f"-{x}{x}{x}",
            f"{x}-{x}{x}",
            f"{x}{x}-{x}"
        ]

        for check in killer_cases:
            # Check rows
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    for j in range(self.cols - 2):
                        if self.board[i][j] == x and self.board[i][j + 1] == x and self.board[i][j + 2] == x:
                            if j - 1 >= 0 and self.board[i][j - 1] == '-':
                                new_board = self.generate_successor('X', i, j - 1)
                                move = j - 1
                            elif j + 3 < self.cols and self.board[i][j + 3] == '-':
                                new_board = self.generate_successor('X', i, j + 3)
                                move = j + 3
                            print("-------- AI -------")
                            new_board.print_board()
                            print(f"AI move: {chr(i + 97)}{move + 1}")
                            print()
                    return True

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    for i in range(self.rows - 2):
                        if self.board[i][j] == x and self.board[i + 1][j] == x and self.board[i + 2][j] == x:
                            if i - 1 >= 0 and self.board[i - 1][j] == '-':
                                new_board = self.generate_successor('X', i - 1, j)
                                move = i - 1
                            elif i + 3 < self.rows and self.board[i + 3][j] == '-':
                                new_board = self.generate_successor('X', i + 3, j)
                                move = i + 3
                            print("-------- AI -------")
                            new_board.print_board()
                            print(f"AI move: {chr(move + 97)}{j + 1}")
                            print()
                    return True
        return False

    def pre_killer_check(self):
        o = 'O'
        x = 'X'

        pre_killer_cases = [
            f"-{x}{x}-",
            f"-{x}-{x}-",
        ]

        check_opponent = [
            f"-{o}{o}{o}-",
            f"{o}{o}{o}-",
            f"-{o}{o}{o}",
            f"{o}-{o}{o}",
            f"{o}{o}-{o}"
        ]

        # Check opponent
        for check in check_opponent:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    return False

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    return False

        # Self check
        for check in pre_killer_cases:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    return True

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    return True

        return False

    def pre_killer_move(self, c):
        x = c

        pre_killer_cases = [
            f"-{x}{x}-",
            f"-{x}-{x}-",
        ]

        for check in pre_killer_cases:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    for j in range(self.cols - 3):
                        if self.board[i][j] == '-' and self.board[i][j + 1] == x and self.board[i][j + 2] == x and self.board[i][j + 3] == '-':
                            if j - 1 >= 0 and self.board[i][j - 1] == '-':
                                new_board = self.generate_successor('X', i, j)
                                print("-------- AI -------")
                                new_board.print_board()
                                print(f"AI move: {chr(i + 97)}{j + 1}")
                                print()
                            elif j + 4 < self.cols and self.board[i][j + 4] == '-':
                                new_board = self.generate_successor('X', i, j + 3)
                                print("-------- AI -------")
                                new_board.print_board()
                                print(f"AI move: {chr(i + 97)}{j + 1 + 3}")
                                print()
                    return new_board

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    for i in range(self.rows - 3):
                        if self.board[i][j] == '-' and self.board[i + 1][j] == x and self.board[i + 2][j] == x and self.board[i + 3][j] == '-':
                            if i - 1 >= 0 and self.board[i - 1][j] == '-':
                                new_board = self.generate_successor('X', i, j)
                                print("-------- AI -------")
                                new_board.print_board()
                                print(f"AI move: {chr(i + 97)}{j + 1}")
                                print()
                            elif i + 4 < self.rows and self.board[i + 4][j] == '-':
                                new_board = self.generate_successor('X', i + 3, j)
                                print("-------- AI -------")
                                new_board.print_board()
                                print(f"AI move: {chr(i + 97 + 3)}{j + 1}")
                                print()
                    return new_board

        return self

    def attack_defense(self):
        attack = 3
        defense = 2
        o = 'O'
        x = 'X'

        defense_cases = [
            f"-{o}{o}{o}-",
            f"{o}{o}{o}-",
            f"-{o}{o}{o}",
            f"{o}-{o}{o}",
            f"{o}{o}-{o}"
        ]

        attack_cases = [
            f"{x}{x}--",
            f"--{x}{x}",
            f"-{x}{x}-",
            f"{x}-{x}-",
            f"-{x}-{x}"
        ]

        for check in defense_cases:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    return defense

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    return defense

        for check in attack_cases:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    return attack

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    return attack

        return attack

    def pre_killer_defense_check(self):
        o = 'O'
        x = 'X'

        self_check = [
            f"-{x}{x}-",
            f"{x}{x}--",
            f"--{x}{x}",
            f"{x}-{x}-",
            f"-{x}-{x}"
        ]

        opponent_pre_killer_cases = [
            f"-{o}{o}--",
            f"--{o}{o}-",
            f"-{o}-{o}-"
        ]

        for check in self_check:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    return False

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    return False

        for check in opponent_pre_killer_cases:
            for i in range(self.rows):
                if check in ''.join(self.board[i]):
                    print("defense 3")
                    return True

            # Check columns
            for j in range(self.cols):
                col = ''.join(self.board[i][j] for i in range(self.rows))
                if check in col:
                    print("defense 4")
                    return True

        return False
