from optimized_matrix.matrix import Matrix

if __name__ == '__main__':
    START = [0, 0];
    END = [3, 3];

    mtr = Matrix()
    grid = mtr.init_grid(4, 4, 3)
    mtr.show_grid()
    mtr.find_a_path(START, END)
    mtr.show_grid()

