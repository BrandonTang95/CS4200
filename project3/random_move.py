
import random

class PreRandomMove:
    def ai_first_move(self, board):
        first_moves = [[3, 3], [3, 4], [4, 3], [4, 4]]
        steps = random.randint(0, 3)
        board = board.generate_successor('X', first_moves[steps][0], first_moves[steps][1])
        print("-------- AI -------")
        board.print_board()
        print(f"AI move: {chr(first_moves[steps][0] + 97)}{first_moves[steps][1] + 1}")
        print()
        return board

    def ai_second_move(self, board):
        Xx, Xy, Ox, Oy = 0, 0, 0, 0
        decision_X, decision_Y = 0, 0

        for i in range(8):
            for j in range(8):
                if board.board[i][j] == 'X':
                    Xx, Xy = i, j
                if board.board[i][j] == 'O':
                    Ox, Oy = i, j

        if Xx == Ox:
            decision_Y = Xy
            if Xx <= 3:
                decision_X = Xx + 1
            else:
                decision_X = Xx - 1

        if Xy == Oy:
            decision_X = Xx
            if Xy <= 3:
                decision_Y = Xy + 1
            else:
                decision_Y = Xy - 1

        # section 1
        if Xx > Ox and Xy > Oy:
            if Xx == 3 and Xy == 3:
                decision_X, decision_Y = 3, 4
            elif Xx == 3 and Xy == 4:
                decision_X, decision_Y = 4, 4
            elif Xx == 4 and Xy == 3:
                decision_X, decision_Y = 4, 4
            elif Xx == 4 and Xy == 4:
                decision_X, decision_Y = 4, 3

        # section 2
        if Xx > Ox and Xy < Oy:
            if Xx == 3 and Xy == 3:
                decision_X, decision_Y = 4, 3
            elif Xx == 3 and Xy == 4:
                decision_X, decision_Y = 3, 3
            elif Xx == 4 and Xy == 3:
                decision_X, decision_Y = 4, 4
            elif Xx == 4 and Xy == 4:
                decision_X, decision_Y = 4, 3

        # section 3
        if Xx < Ox and Xy > Oy:
            if Xx == 3 and Xy == 3:
                decision_X, decision_Y = 3, 4
            elif Xx == 3 and Xy == 4:
                decision_X, decision_Y = 3, 3
            elif Xx == 4 and Xy == 3:
                decision_X, decision_Y = 4, 4
            elif Xx == 4 and Xy == 4:
                decision_X, decision_Y = 3, 4

        # section 4
        if Xx < Ox and Xy < Oy:
            if Xx == 3 and Xy == 3:
                decision_X, decision_Y = 3, 4
            elif Xx == 3 and Xy == 4:
                decision_X, decision_Y = 3, 3
            elif Xx == 4 and Xy == 3:
                decision_X, decision_Y = 3, 3
            elif Xx == 4 and Xy == 4:
                decision_X, decision_Y = 3, 4

        board = board.generate_successor('X', decision_X, decision_Y)
        print("-------- AI -------")
        board.print_board()
        print(f"AI move: {chr(decision_X + 97)}{decision_Y + 1}")
        print()
        return board

    def ai_connect_move(self, board):
        Xx, Xy, Ox, Oy = 0, 0, 0, 0
        decision_X, decision_Y = 0, 0

        for i in range(8):
            for j in range(8):
                if board.board[i][j] == 'O':
                    Ox, Oy = i, j

        if Ox < 4 and Oy < 4:
            if 7 - Ox > 7 - Oy:
                decision_X, decision_Y = Ox + 1, Oy
            else:
                decision_X, decision_Y = Ox, Oy + 1

        elif Ox < 4 and Oy >= 4:
            if 7 - Ox > Oy:
                decision_X, decision_Y = Ox + 1, Oy
            else:
                decision_X, decision_Y = Ox, Oy - 1

        elif Ox >= 4 and Oy < 4:
            if Ox > 7 - Oy:
                decision_X, decision_Y = Ox - 1, Oy
            else:
                decision_X, decision_Y = Ox, Oy + 1

        elif Ox >= 4 and Oy >= 4:
            if Ox > Oy:
                decision_X, decision_Y = Ox - 1, Oy
            else:
                decision_X, decision_Y = Ox, Oy - 1

        board = board.generate_successor('X', decision_X, decision_Y)
        print("-------- AI -------")
        board.print_board()
        print(f"AI move: {chr(decision_X + 97)}{decision_Y + 1}")
        print()
        return board
