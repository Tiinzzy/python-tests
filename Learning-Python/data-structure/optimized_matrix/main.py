from optimized_matrix.matrix import Matrix

if __name__ == '__main__':
    START = [0, 0]
    END = [4, 4]
    ITERATION = []

    for _ in range(500):
        mtr = Matrix()
        mtr.init_grid(5, 5, 3)
        mtr.show_grid()
        result = mtr.find_a_path(START, END)
        if result['result']:
            mtr.show_grid()
            print(result)
