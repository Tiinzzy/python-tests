import random
import numpy as np
import time

FREE = 0
START = 1
PATH = 2
END = 9
BLOCKED = 8


class Matrix:
    def __init__(self):
        random.seed(time.time() * 1000)
        self.grid = None
        self.rows = None
        self.columns = None
        self.blocked = None

    def init_grid(self, rows, cols, blocked):
        g = [[FREE for _ in range(cols)] for _ in range(rows)]

        while self._grid_sum(g) < blocked * BLOCKED:
            r = self._get_random_int(rows)
            c = self._get_random_int(cols)
            g[r][c] = BLOCKED
        self.grid = self._clone_2d_array(g)
        self.rows = rows
        self.columns = cols
        self.blocked = blocked
        return g

    def find_a_path(self, start, end):
        path = [start]
        result = False

        if self.grid[start[0]][start[1]] != FREE:
            return {"path": path, "grid": self.grid, "result": result}

        if self.grid[end[0]][end[1]] != FREE:
            return {"path": path, "grid": self.grid, "result": result}

        self.grid[start[0]][start[1]] = START
        self.grid[end[0]][end[1]] = END

        current = start
        while not self._ceq(current, end):
            next_cell = self._get_next_cell(self.grid, current)
            if next_cell is None:
                break
            elif self._ceq(next_cell, end):
                path.append(end)
                result = True
                break
            else:
                current = next_cell
                path.append(current)
                self.grid[current[0]][current[1]] = PATH

        return {"path": path, "result": result, 'grid': np.array(self.grid)}

    @staticmethod
    def _clone_2d_array(array):
        return [row[:] for row in array]

    @staticmethod
    def _grid_sum(grid):
        return sum(sum(row) for row in grid)

    @staticmethod
    def _get_random_int(max_val):
        return random.randint(0, max_val - 1)

    @staticmethod
    def _ceq(a, b):
        return a[0] == b[0] and a[1] == b[1]

    @staticmethod
    def _get_next_cell(grid, current):
        options = []
        top = [current[0] - 1, current[1]]
        if top[0] >= 0 and (grid[top[0]][top[1]] == FREE or grid[top[0]][top[1]] == END):
            options.append(top)

        right = [current[0], current[1] + 1]
        if right[1] < len(grid[0]) and (grid[right[0]][right[1]] == FREE or grid[right[0]][right[1]] == END):
            options.append(right)

        bottom = [current[0] + 1, current[1]]
        if bottom[0] < len(grid) and (grid[bottom[0]][bottom[1]] == FREE or grid[bottom[0]][bottom[1]] == END):
            options.append(bottom)

        left = [current[0], current[1] - 1]
        if left[1] >= 0 and (grid[left[0]][left[1]] == FREE or grid[left[0]][left[1]] == END):
            options.append(left)

        if options:
            return random.choice(options)
        else:
            return None

    def show_grid(self):
        print(np.array(self.grid))
