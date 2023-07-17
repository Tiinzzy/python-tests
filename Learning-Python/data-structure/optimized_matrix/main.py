from optimized_matrix.matrix import Matrix


def find_shortest_path(array_of_objects):
    min_object = None
    min_value = float('inf')

    for obj in array_of_objects:
        if 'length' in obj and obj['length'] < min_value:
            min_value = obj['length']
            min_object = obj
    return min_object


if __name__ == '__main__':
    START = [0, 0]
    END = [4, 5]
    ITERATION = []

    for _ in range(500):
        mtr = Matrix()
        mtr.init_grid(6, 10, 3)
        result = mtr.find_a_path(START, END)
        if result['result']:
            length = len(result['path'])
            ITERATION.append({'length': length, 'data': result})

    shortest = find_shortest_path(ITERATION)
    print('-----------')
    print(shortest['data']['grid'])
    print('path -->',shortest['data']['path'])
    print('length -->', shortest['length'])
