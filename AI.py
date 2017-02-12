from sys import maxsize
from Engine import TicTacToe


class Computer:

    def __init__(self, depth, board, isMax, alpha, beta):
        self.depth = depth
        self.board = board
        self.alpha = alpha
        self.beta = beta
        self.isMax = isMax

        def minmax(self):
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
                                    bestscore, self.minmax(depth + 1, not isMax, self.alpha, self.beta))
                                self.board[y][x] = None
                                self.alpha = max(self.alpha, bestscore)
                                if self.beta <= self.alpha:
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
                                self.beta = min(self.beta, bestscore)
                                if self.beta <= self.alpha:
                                    break
                    return bestscore + depth

        def getBestMove(self, alpha, beta):
            bestval = maxsize * -1
            row = -1
            column = -1

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
