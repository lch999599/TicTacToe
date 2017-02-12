from sys import maxsize
# -1 = x ; 1 = o


class TicTacToe:

    def __init__(self, board, length, winning_combo, depth):
        self.board = board
        self.length = length
        self.winning_combo = winning_combo
        self.player = 1
        self.depth = depth
        self.count = 0

    def isGameOver(self):
        for y in range(0, self.length):
            for x in range(0, self.length):
                if self.board[y][x] is None:
                    return False
        return True

    def paintBoard(self):
        printed_board = "-" * (self.length * 4 + 1) + '\n'
        for y in range(0, self.length):
            for x in range(0, self.length):
                state = self.board[y][x]
                if state is None:
                    printed_board += '|   '
                elif state == -1:
                    printed_board += '| X '
                elif state == 1:
                    printed_board += '| O '
            printed_board += ('|\n' + "-" * (self.length * 4 + 1) + '\n')
        return printed_board

    def checkWin(self):
        # horizontal check
        combo = 0
        for y in range(0, self.length):
            for x in range(0, self.length - 1):
                last = self.board[y][x]
                if last == self.board[y][x + 1] and self.board[y][x] is not None:
                    combo += 1
                    if combo == self.winning_combo - 1:
                        # print("horizontal")
                        return self.board[y][x] * maxsize
                else:
                    combo = 0

        # vertical check
        combo = 0
        for x in range(0, self.length):
            for y in range(0, self.length - 1):
                last = self.board[y][x]
                if last == self.board[y + 1][x] and self.board[y][x] is not None:
                    combo += 1
                    if combo == self.winning_combo - 1:
                        # print("vertical")
                        return self.board[y][x] * maxsize
                else:
                    combo = 0

        # diagonal right check
        combo = 0
        for y in range(0, self.length):
            for x in range(0, self.length):
                last = self.board[y][x]
                for i in range(0, self.winning_combo):
                    try:
                        if last == self.board[y + i][x + i] and self.board[y][x] is not None:
                            combo += 1
                            if combo == self.winning_combo:
                                #print("diag right")
                                return self.board[y][x] * maxsize
                        else:
                            combo = 0
                            break
                    except IndexError:
                        combo = 0
                        break

        # diagonal left check
        combo = 0
        for y in range(0, self.length):
            for x in range(0, self.length):
                last = self.board[y][x]
                for i in range(0, self.winning_combo):
                    try:
                        if last == self.board[y + i][x - i] and x - i >= 0 and self.board[y][x] is not None:
                            combo += 1
                            if combo == self.winning_combo:
                                #print("diag left")
                                return self.board[y][x] * maxsize
                        else:
                            combo = 0
                            break
                    except IndexError:
                        combo = 0
                        break
        return 0

    def capturePoint(self, cord):
        if self.checkWin() == 0:
            if self.board[int(cord[1])][int(cord[0])] is None:
                self.board[int(cord[1])][int(cord[0])] = - \
                    1 if self.player % 2 == 0 else 1
                self.player += 1
            else:
                print("You Filthy Cheater!")
        else:
            print("Game Over!")

    def minmax(self, depth, isMax, alpha, beta):
        bestscore = 0
        if depth == self.depth:
            return bestscore
        else:
            self.count += 1
            score = self.checkWin()
            if abs(score) == maxsize:
                return score

            if self.isGameOver():
                return 0

            if isMax:
                bestscore = maxsize * -1
                for y in range(0, self.length):
                    for x in range(0, self.length):
                        if self.board[y][x] is None:
                            self.board[y][x] = 1
                            bestscore = max(
                                bestscore, self.minmax(depth + 1, not isMax, alpha, beta))
                            self.board[y][x] = None
                            alpha = max(alpha, bestscore)
                            if beta <= alpha:
                                break
                return bestscore - depth
            else:
                bestscore = maxsize
                for y in range(0, self.length):
                    for x in range(0, self.length):
                        if self.board[y][x] is None:
                            self.board[y][x] = -1
                            bestscore = min(
                                bestscore, self.minmax(depth + 1, not isMax, alpha, beta))
                            self.board[y][x] = None
                            beta = min(beta, bestscore)
                            if beta <= alpha:
                                break
                return bestscore + depth

    def getBestMove(self, alpha, beta):
        bestval = maxsize * -1
        row = None
        column = None

        for y in range(0, self.length):
            for x in range(0, self.length):
                if self.board[y][x] is None:
                    self.board[y][x] = 1
                    value = self.minmax(0, False, alpha, beta)
                    self.board[y][x] = None
                    if value > bestval:
                        row = y
                        column = x
                        bestval = value
        print(row)
        print(column)
        if self.player % 2 != 0 and (row or column) != None:
            self.capturePoint(str(column) + str(row))
        else:
            print("You win! The computer gave up")
