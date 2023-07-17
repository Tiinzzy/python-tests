import numpy as np
from optimized_matrix.matrix import Matrix

FREE = 0
START = 1
PATH = 2
END = 9
BLOCKED = 8


def find_shortest_path(array_of_objects):
    min_object = None
    min_value = float('inf')

    for obj in array_of_objects:
        if 'length' in obj and obj['length'] < min_value:
            min_value = obj['length']
            min_object = obj
    return min_object


def pretty_print_all(grid, start, end, iteration):
    grid[start[0]][start[1]] = START
    grid[end[0]][end[1]] = END

    for i in range(1, len(iteration["path"]) - 1):
        grid[iteration["path"][i][0]][iteration["path"][i][1]] = get_path_arrow(iteration["path"][i],
                                                                                iteration["path"][i + 1])

    row_up = "┌─" + "──┬─" * (len(grid[0]) - 1) + "──┐"
    print(row_up)

    for r in range(len(grid)):
        row = "│ " + " │ ".join(to_cell_char(grid[r][c]) for c in range(len(grid[r]))) + " │ "
        row_down = "├─" + "──┼─" * (len(grid[r]) - 1) + "──┤" if r < len(grid) - 1 else "└─" + "──┴─" * (
                len(grid[r]) - 1) + "──┘"
        print(row)
        print(row_down)


def get_path_arrow(from_cell, to_cell):
    if from_cell[0] == to_cell[0] and from_cell[1] == to_cell[1] - 1:
        return '→'
    elif from_cell[0] == to_cell[0] and from_cell[1] == to_cell[1] + 1:
        return '←'
    elif from_cell[0] == to_cell[0] - 1 and from_cell[1] == to_cell[1]:
        return '↓'
    elif from_cell[0] == to_cell[0] + 1 and from_cell[1] == to_cell[1]:
        return '↑'
    return '?'


def to_cell_char(cell_id):
    if cell_id == FREE:
        return " "
    elif cell_id == START:
        return "○"
    elif cell_id == END:
        return "●"
    elif cell_id == BLOCKED:
        return "▩"
    else:
        return str(cell_id)


if __name__ == '__main__':
    START = [0, 0]
    END = [5, 5]
    ITERATION = []

    for _ in range(1000):
        mtr = Matrix()
        mtr.init_grid(6, 6, 4)
        result = mtr.find_a_path(START, END)
        if result['result']:
            length = len(result['path'])
            ITERATION.append({'length': length, 'data': result})

    for _ in ITERATION:
        print(_['length'])
    shortest = find_shortest_path(ITERATION)

    print('-----------')
    print(np.array(shortest['data']['grid']))
    print('path -->', shortest['data']['path'])
    print('length -->', shortest['length'])

    pretty_print_all(shortest['data']['grid'], START, END, shortest['data'])
