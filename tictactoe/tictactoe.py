"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


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
    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                moves.append((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]
    if new_board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    else:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = board
    if board[0][0] == board[0][1] == board[0][2] is not EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] is not EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] is not EMPTY:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] is not EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] is not EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] is not EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] is not EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] is not EMPTY:
        return board[0][2]
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board = board
    if winner(board) is not None:
        return True
    elif board[0][0] is not EMPTY and board[0][1] is not EMPTY and board[0][2] is not EMPTY and board[1][0] is not EMPTY and board[1][1] is not EMPTY and board[1][2] is not EMPTY and board[2][0] is not EMPTY and board[2][1] is not EMPTY and board[2][2] is not EMPTY:
        return True
    else:
        return False
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    moves = []
    current_player = player(board)
    
    if current_player == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > v:
                v = value
                best_action = action
        return best_action
    else:
        v = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < v:
                v = value
                best_action = action
        return best_action

    raise NotImplementedError
