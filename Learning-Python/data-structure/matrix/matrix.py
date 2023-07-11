import numpy as np
import random


class Matrix:
    def __init__(self):
        self.grid = None

    def random_insert(self, size, fill_in):
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
            return None
        else:
            grid = self.grid.tolist()
            for row in grid:
                for column in row:
                    if column == start[1] and column != 1:
                        self._find_path(grid, start, destination)
                    else:
                        return None

    def _find_path(self, grid, start, destination):
        pass
        # check for corners
        # check for not having 1
        # save the previous path came from
        #          [2,0]
        # [3,-1] < [3,0] > [3,1]
        #          [4,0]