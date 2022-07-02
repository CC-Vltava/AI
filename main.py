import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

posx = [-1, -1, -1, 0, 0, 1, 1, 1]
posy = [-1, 0, 1, -1, 1, -1, 0, 1]

range_x = 7
range_y = 7


def check_position_illegal(x, y):
    return 0 <= x <= range_x and 0 <= y <= range_y


def check_direction(chessboard, x, y, direction, b, w, color):
    if not check_position_illegal(x, y):
        return False
    if chessboard[x][y] == COLOR_NONE:
        return False
    if chessboard[x][y] == COLOR_BLACK:
        b = b + 1
    else:
        w = w + 1

    if color == COLOR_WHITE and w == 2:
        return b
    if color == COLOR_BLACK and b == 2:
        return w
    return check_direction(chessboard, x + posx[direction], y + posy[direction], direction, b, w, color)


def check_pos(chessboard, x, y, color):
    for i in range(8):
        if check_direction(chessboard, x, y, i, 0, 0, color):
            return True
    return False


def edge(s):
    x = s[0]
    y = s[1]
    return x == 0 or x == range_x or y == 0 or y == range_y


def mhd_dis(x, y, fx, fy):
    return abs(x - fx) + abs(y - fy)


def dis(chessboard, x, y, color):
    ans = 123123123
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if chessboard[i][j] == color:
                ans = min(ans, mhd_dis(i, j, x, y))
    return ans


def cost(chessboard, x, y, color):
    ans = 0
    for i in range(8):
        ans += check_pos(chessboard, x, y, color)
    return ans


def tot(chessboard):
    ans = 0
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if chessboard[i][j] != COLOR_NONE:
                ans = ans + 1
    return ans


# don't change the class name
class AI(object):

    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list
        # System will get the end of your candidate_list as your decision .
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
            if check_pos(chessboard, pos[0], pos[1], self.color):
                self.candidate_list.append(pos)
            chessboard[pos[0]][pos[1]] = 0

        # 到这里已经让所有可能的答案放在self.candidate_list里面

        min_dis = 123123123
        save = []

        for pos in self.candidate_list:
            min_dis = min(min_dis, dis(chessboard, pos[0], pos[1], self.color))

        for pos in self.candidate_list:
            if dis(chessboard, pos[0], pos[1], self.color) - min_dis <= 1:
                save.append(pos)

        ans = (-1, -1)
        for pos in save:
            if ans == (-1, -1):
                ans = pos
            if edge(ans) and not edge(pos):
                ans = pos
            if cost(chessboard, ans[0], ans[1], self.color) >= cost(chessboard, pos[0], pos[1], self.color):
                ans = pos

        if ans == (-1, -1):
            return

        for i in range(len(self.candidate_list)):
            if self.candidate_list[i] == ans and random.random() > 0.1:
                t = self.candidate_list[len(self.candidate_list) - 1]
                self.candidate_list[len(self.candidate_list) - 1] = ans
                self.candidate_list[i] = t
                break

        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, the system will return error.
        # Add your decision into candidate_list, Records the chess board
        # You need add all the positions which is valid
        # candidate_list example: [(3,3),(4,4)]

        # You need append your decision at the end of the candidate_list,
        # we will pickthe last element of the candidate_list as the position you choose
        # If there is no valid position, you must return an empty list.
