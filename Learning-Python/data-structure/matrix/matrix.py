import numpy as np
import random
import time


class Matrix:
    def __init__(self):
        self.grid = None
        self.size = None

    def random_insert(self, size, fill_in):
        self.size = size
        random.seed(time.time())
        random_array = np.zeros(size, dtype=int)
        while np.sum(random_array) < fill_in:
            r = random.randint(0, size[0] - 1)
            c = random.randint(0, size[1] - 1)
            random_array[r, c] = 1
        self.grid = random_array

    def show_grid(self):
        print(self.grid)

    def path_to_destination(self, start, destination):
        if start is None or destination is None:
            return False
        else:
            grid = self.grid.tolist()
            return self._find_path(grid, start, destination)

    def _find_path(self, grid, start, destination):
        r = start[0]
        c = start[1]
        path = [start]
        begin = True
        while begin:
            top_status, top_path = self._get_top_status(r, c, grid, destination)
            bottom_status, bottom_path = self._get_bottom_status(r, c, grid, destination)
            right_status, right_path = self._get_right_status(r, c, grid, destination)
            left_status, left_path = self._get_left_status(r, c, grid, destination)
            direction = self._pick_direction(top_status, top_path, bottom_status, bottom_path, right_status, right_path,
                                             left_status, left_path)
            grid[r][c] = -1
            r = direction[0]
            c = direction[1]
            path.append(direction)
            row, col = direction
            if direction == (-1, -1):
                # print('DEADEND')
                # print(np.array(grid))
                # path.clear()
                # self._find_path(self.grid.tolist(), start, destination)
                # print(np.array(grid))
                return False, path
            if [r, c] == destination or [row, col] == destination:
                begin = False
                # print('SOLVED!')
                grid[r][c] = -1
                print(np.array(grid))
                return True, path
        return False, path

    @staticmethod
    def _pick_direction(top, top_path, bottom, bottom_path, right, right_path, left, left_path):
        options = []
        options.clear()
        if top:
            options.append(top_path)
        if bottom:
            options.append(bottom_path)
        if right:
            options.append(right_path)
        if left:
            options.append(left_path)

        if len(options) == 0:
            return (-1, -1)
        elif len(options) == 1:
            return options[0]
        else:
            rand_choice = random.randint(0, len(options) - 1)
            rand_opt = options[rand_choice]
            return rand_opt

    @staticmethod
    def _get_top_status(row, col, matrix, destination):
        top_r = row - 1
        top_c = col
        top_ok = True
        if top_r < 0 or matrix[top_r][top_c] != 0:
            # or destination == [top_r, top_c]:
            top_ok = False
        return top_ok, (top_r, top_c)

    def _get_bottom_status(self, row, col, matrix, destination):
        bottom_r = row + 1
        bottom_c = col
        bot_ok = True
        if bottom_r >= self.size[0] or matrix[bottom_r][bottom_c] != 0:
            # or destination == [bottom_r, bottom_c]:
            bot_ok = False
        return bot_ok, (bottom_r, bottom_c)

    def _get_right_status(self, row, col, matrix, destination):
        right_r = row
        right_c = col + 1
        right_ok = True
        if right_c >= self.size[1] or matrix[right_r][right_c] != 0:
            # or destination == [right_r, right_c]:
            right_ok = False
        return right_ok, (right_r, right_c)

    @staticmethod
    def _get_left_status(row, col, matrix, destination):
        left_r = row
        left_c = col - 1
        left_ok = True
        if left_c < 0 or matrix[left_r][left_c] != 0:
            # or destination == [left_r, left_c]:
            left_ok = False
        return left_ok, (left_r, left_c)

    def brute_force_check(self, start, end, count, strategy):
        # if destination is 1 not solvable
        # check first house is also 0 and not 1
        pass

    # before choosing random direction try the previously selected direction
    # if more than one option choose the previuos
    # save previous direction if went before
    # save paths and choose the one with shortest length
    # when you solved the problem, do not stop looking for other solutions, finally return the shortest path
    # previously select(more than 1 option)/ not previously selected(more than 1 option)/ random selection