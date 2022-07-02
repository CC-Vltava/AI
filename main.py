import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

posx = [-1, -1, -1, 0, 0, 1, 1, 1]
posy = [-1, 0, 1, -1, 1, -1, 0, 1]


def check_position_illegal(x, y, size):
    return 0 <= x < size and 0 <= y < size


def check_direction(chessboard, x, y, direction, b, w, color, size):
    if not check_position_illegal(x, y, size):
        return False
    if chessboard[x][y] == COLOR_NONE:
        return False
    if chessboard[x][y] == COLOR_BLACK:
        b = b + 1
    else:
        w = w + 1

    if color == COLOR_WHITE and w == 2:
        return b > 0
    if color == COLOR_BLACK and b == 2:
        return w > 0
    return check_direction(chessboard, x + posx[direction], y + posx[direction], direction, b, w, color, size)


def check_pos(chessboard, x, y, color, size):
    for i in range(8):
        if check_direction(chessboard, x, y, i, 0, 0, color, size):
            return True
    return False


# don't change the class name
class AI(object):

    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision.
        self.candidate_list = []

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        for pos in idx:
            chessboard[pos[0]][pos[1]] = self.color
            if check_pos(chessboard, pos[0], pos[1], self.color, self.chessboard_size):
                self.candidate_list.append(pos)
            chessboard[pos[0]][pos[1]] = 0

        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]

        # You need append your decision at the end of the candidate_list,
        # we will pick the last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
