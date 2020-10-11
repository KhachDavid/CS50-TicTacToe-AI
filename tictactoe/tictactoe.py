"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def main():
    print(result([["X", EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY]], (1, 2)))
    print(winner([["O", "X", "O"],
                  ["O", "X", "O"],
                  ["X", "O", "X"]]))
    print(terminal([["X", "O", "O"],
                    ["O", "O", "X"],
                    ["X", "X", "X"]]))


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # initializing the number of x and o on the board
    xCounter = 0
    oCounter = 0

    # iteration over the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                xCounter += 1
            if board[i][j] == "O":
                oCounter += 1

    # the logic is that if there is
    # an equal amount of "X"s and "O"s
    # it would be X's turn to play
    if xCounter == oCounter:
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    returnSet = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X' and board[i][j] != 'O':
                tup = (i, j)
                returnSet.add(tup)

    return returnSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # check for an illegal move
    if action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise Exception("Illegal Move")

    # create a deep copy of the current board
    returnList = copy.deepcopy(board)

    # change the given index to either "X" or "O"
    # Depends on the return of player()
    returnList[int(action[0])][int(action[1])] = player(board)

    return returnList


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_winner(board, 'X') == 'X':
        return 'X'
    if check_winner(board, 'O') == 'O':
        return 'O'
    return None


def check_winner(board, x):
    if board[0][0] == x and board[1][0] == x and board[2][0] == x:
        return x
    elif [x, x, x] in board:
        return x
    elif board[0][1] == x and board[1][1] == x and board[2][1] == x:
        return x
    elif board[0][2] == x and board[1][2] == x and board[2][2] == x:
        return x
    elif board[0][0] == x and board[1][1] == x and board[2][2] == x:
        return x
    elif board[0][2] == x and board[1][1] == x and board[2][0] == x:
        return x


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'X' or board[row][col] == 'O':
                counter += 1

    if counter == len(board) * len(board[0]) or winner(board) is not None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1

    if winner(board) == 'O':
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == 'X':
        val, returnValue = max_value(board)
        return returnValue
    if player(board) == 'O':
        val, returnValue = min_value(board)
        return returnValue


def max_value(board):
    if terminal(board):
        return utility(board), None

    returnValue = None
    v = -1000

    for action in actions(board):
        index, ret = min_value(result(board, action))
        if index > v:
            v = index
            returnValue = action
            if index == 1:
                return index, returnValue
    return v, returnValue


def min_value(board):
    if terminal(board):
        return utility(board), None

    returnValue = None
    v = 1000

    for action in actions(board):
        index, ret = max_value(result(board, action))
        if index < v:
            v = index
            returnValue = action
            if index == -1:
                return index, returnValue
    return v, returnValue


if __name__ == '__main__':
    main()
