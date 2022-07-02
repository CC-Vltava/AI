import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

posx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
posy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

range_x = 7
range_y = 7


def check_position_illegal(x, y):
    return 0 <= x <= range_x and 0 <= y <= range_y


def check_direction(chessboard, x, y, direction, b, w, sta):
    if not check_position_illegal(x, y):
        return False
    if chessboard[x][y] == 0:
        return 0
    if chessboard[x][y] == 1:
        w = w + 1
    else:
        b = b + 1
    if b + w == 1:
        sta = chessboard[x][y]
    if sta == 1 and w == 2:
        return b > 0
    if sta == -1 and b == 2:
        return w > 0
    return check_direction(chessboard, x + posx[direction], y + posx[direction], direction, b, w, sta)


def check_pos(chessboard, x, y):
    for i in range(8):
        if check_direction(chessboard, x, y, i, 0, 0, 0):
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
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
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
        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]



        # You need append your decision at the end of the candidate_list,
        # we will pickthe last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
