from Engine import TicTacToe
from sys import maxsize


def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    length = 5
    winning_combo = 4
    header = '|'
    board = [[None for y in range(length)] for x in range(length)]
    game = TicTacToe(board, length, winning_combo, 6)
    for i in range(0, length):
        header += (" %s |" % (alphabet[i]))
    print(header)
    print(game.paintBoard())
    while True:
        game.getBestMove(-maxsize, maxsize)
        print(header)
        print(game.paintBoard())
        user = input()
        user = str(alphabet.index(user[0])) + str(int(user[1]) - 1)

        game.capturePoint(user)

        print(game.checkWin())
        print(header)
        print(game.paintBoard())

if __name__ == '__main__':
    main()
