
from board import Board
from minimax import MiniMaxAgent
from random_move import PreRandomMove
from score_point import PointScore

class Main:
    def __init__(self):
        pass

    def main(self):
        print("*** Start Game Connect Four ***")
        print()

        time_limit = int(input("Enter the maximum running time (this program is required in 25 seconds): "))
        depth = int(input("Enter the depth: "))
        order = input("Who goes first ( 'C' for Computer AI, 'O' for Opponent ): ").upper()

        while order not in ['C', 'O']:
            order = input("Please enter a correct first hand ( 'C' for Computer AI, 'O' for Opponent ): ").upper()

        print()
        print("    -- Game Start --")
        print("****************************")
        print(f"|  -Maximum time (sec): {time_limit} |")
        print(f"|  -Game Depth: {depth}          |")
        print(f"|  -First Hand: {'AI' if order == 'C' else 'Human'}     |")
        print("****************************")
        print()
        print("---Initial Board---")

        agent = MiniMaxAgent(depth)
        board = Board()
        board.print_board()
        print()

        if order == 'C':
            pre_move = PreRandomMove()
            board = pre_move.ai_first_move(board)
            board = self.human_move(board)
            board = pre_move.ai_second_move(board)
            board = self.human_move(board)
        else:
            pre_move = PreRandomMove()
            board = self.human_move(board)
            board = pre_move.ai_connect_move(board)
            board = self.human_move(board)

        while True:
            if board.killer_check():
                print("AI win")
                break

            pre_killer_check = board.pre_killer_check()
            if pre_killer_check:
                print("in1")
                board = board.pre_killer_move('X')

            pre_killer_defense_check = board.pre_killer_defense_check()
            if not pre_killer_check and pre_killer_defense_check:
                board = board.pre_killer_move('O')

            agent.set_depth(board.attack_defense())
            if not pre_killer_check and not pre_killer_defense_check:
                board = agent.action(board)

            if board.is_goal('X'):
                print("AI win")
                break

            board = self.human_move(board)

            if board.is_goal('O'):
                print("Opponent win")
                break

            if board.is_draw():
                print("Draw !")
                break

    def human_move(self, board):
        row, col = 0, 0
        c = 'O'

        temp = input("==================> Enter your next move: ")
        splitted = list(temp)

        row = ord(splitted[0]) - 97
        col = int(splitted[1]) - 1

        while not board.input_check(row, col):
            print()
            print("The move you want is not valid !!!")
            print()
            temp = input("==================> Enter your next move: ")
            splitted = list(temp)
            row = ord(splitted[0]) - 97
            col = int(splitted[1]) - 1

        board = board.generate_successor(c, row, col)
        print()
        print("----- OPPONENT ----")
        board.print_board()
        print(f"Human move: {splitted[0]}{splitted[1]}")
        print()

        return board

if __name__ == "__main__":
    Main().main()
