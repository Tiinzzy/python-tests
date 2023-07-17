import random
import numpy as np

FREE = 0
START = 1
PATH = 2
END = 9
BLOCKED = 8


class Matrix:
    def __init__(self):
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
        self.grid = g
        self.rows = rows
        self.columns = cols
        self.blocked = blocked
        return g

    @staticmethod
    def _grid_sum(grid):
        return sum(sum(row) for row in grid)

    @staticmethod
    def _get_random_int(max_val):
        return random.randint(0, max_val - 1)

    def show_grid(self):
        print(np.array(self.grid))
