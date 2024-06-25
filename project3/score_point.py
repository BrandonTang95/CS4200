
class PointScore:
    def __init__(self):
        self.result = 0

    def score_point(self, board, x, y, c):
        count = 1
        block = 0
        empty = -1

        # check the rows
        for i in range(y + 1, len(board)):
            if i >= 8:
                block += 1
                break
            if board[x][i] == '-':
                if empty == -1 and i < 7 and board[x][i + 1] == c:
                    empty = count
                    continue
                else:
                    break
            if board[x][i] == c:
                count += 1
                continue
            else:
                block += 1
                break

        for i in range(y - 1, -1, -1):
            if i < 0:
                block += 1
                break
            if board[x][i] == '-':
                if empty == -1 and i > 0 and board[x][i - 1] == c:
                    empty = 0
                    continue
                else:
                    break
            if board[x][i] == c:
                count += 1
                if empty != -1:
                    empty += 1
                continue
            else:
                block += 1
                break

        self.result += self.calculate_score(empty, count, block)

        count = 1
        block = 0
        empty = -1

        # check the columns
        for i in range(x + 1, len(board)):
            if i >= 8:
                block += 1
                break
            if board[i][y] == '-':
                if empty == -1 and i < 7 and board[i + 1][y] == c:
                    empty = count
                    continue
                else:
                    break
            if board[i][y] == c:
                count += 1
                continue
            else:
                block += 1
                break

        for i in range(x - 1, -1, -1):
            if i < 0:
                block += 1
                break
            if board[i][y] == '-':
                if empty == -1 and i > 0 and board[i - 1][y] == c:
                    empty = 0
                    continue
                else:
                    break
            if board[i][y] == c:
                count += 1
                if empty != -1:
                    empty += 1
                continue
            else:
                block += 1
                break

        self.result += self.calculate_score(empty, count, block)

        return self.result

    def calculate_score(self, empty, count, block):
        if empty <= 0:
            if count >= 4:
                return 1000
            if block == 0:
                if count == 1:
                    return 10
                if count == 2:
                    return 100
                if count == 3:
                    return 1000
            if block == 1:
                if count == 1:
                    return 5
                if count == 2:
                    return 50
                if count == 3:
                    return 500
            if block == 2:
                if count == 1:
                    return 2
                if count == 2:
                    return 25
                if count == 3:
                    return 250
        elif empty == 1:
            if count >= 5:
                return 1000
            if block == 0:
                if count == 2:
                    return 20
                if count == 3:
                    return 110
                if count == 4:
                    return 1000
            if block == 1:
                if count == 2:
                    return 15
                if count == 3:
                    return 105
                if count == 4:
                    return 505
            if block == 2:
                if count == 2:
                    return 12
                if count == 3:
                    return 102
                if count == 4:
                    return 502
        elif empty == 2:
            if count >= 6:
                return 1000
            if block == 0:
                if count == 3:
                    return 110
                if count == 4:
                    return 200
                if count == 5:
                    return 1000
            if block == 1:
                if count == 3:
                    return 105
                if count == 4:
                    return 150
                if count == 5:
                    return 510
            if block == 2:
                if count == 3:
                    return 102
                if count == 4:
                    return 125
                if count == 5:
                    return 505
        elif empty == 3:
            if count >= 7:
                return 1000
            if block == 0:
                if count == 4:
                    return 1000
                if count == 5:
                    return 1000
                if count == 6:
                    return 1000
            if block == 1:
                if count == 4:
                    return 505
                if count == 5:
                    return 510
                if count == 6:
                    return 115
            if block == 2:
                if count == 4:
                    return 502
                if count == 5:
                    return 505
                if count == 6:
                    return 1000
        return 0
